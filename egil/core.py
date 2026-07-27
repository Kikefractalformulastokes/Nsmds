"""Core EGIL operators for NS-MDS.

The module deliberately uses only the Python standard library so that the
first operational milestone is easy to reproduce and audit.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import cos, sin, sqrt
from typing import Iterable, Sequence

Vector2 = tuple[float, float]


@dataclass(frozen=True)
class Frame2D:
    """Rigid 2-D reference frame with optional uniform scale and translation."""

    angle_rad: float = 0.0
    scale: float = 1.0
    translation: Vector2 = (0.0, 0.0)

    def __post_init__(self) -> None:
        if self.scale <= 0.0:
            raise ValueError("scale must be strictly positive")

    def transform(self, point: Vector2) -> Vector2:
        x, y = point
        c, s = cos(self.angle_rad), sin(self.angle_rad)
        xr = self.scale * (c * x - s * y) + self.translation[0]
        yr = self.scale * (s * x + c * y) + self.translation[1]
        return xr, yr

    def inverse(self, point: Vector2) -> Vector2:
        x = (point[0] - self.translation[0]) / self.scale
        y = (point[1] - self.translation[1]) / self.scale
        c, s = cos(self.angle_rad), sin(self.angle_rad)
        return c * x + s * y, -s * x + c * y


def _l2(values: Iterable[float]) -> float:
    return sqrt(sum(value * value for value in values))


def frame_consistency_error(
    reference_predictions: Sequence[Vector2],
    transformed_predictions: Sequence[Vector2],
    frame: Frame2D,
    epsilon: float = 1e-12,
) -> float:
    """Return normalized error after mapping transformed predictions back.

    A perfectly frame-consistent model obtains zero.
    """
    if len(reference_predictions) != len(transformed_predictions):
        raise ValueError("prediction sequences must have identical length")
    if not reference_predictions:
        raise ValueError("prediction sequences must not be empty")

    residuals: list[float] = []
    reference_flat: list[float] = []
    for reference, transformed in zip(reference_predictions, transformed_predictions):
        recovered = frame.inverse(transformed)
        residuals.extend((recovered[0] - reference[0], recovered[1] - reference[1]))
        reference_flat.extend(reference)
    return _l2(residuals) / (_l2(reference_flat) + epsilon)


@dataclass(frozen=True)
class ConservationState:
    """Compact control-volume state used by the v0 conservation audit."""

    mass: float
    momentum: Vector2
    energy: float


def conservation_residual(
    before: ConservationState,
    after: ConservationState,
    mass_flux: float = 0.0,
    momentum_flux: Vector2 = (0.0, 0.0),
    energy_flux: float = 0.0,
) -> ConservationState:
    """Compute balance residuals: after - before - externally supplied flux."""
    return ConservationState(
        mass=after.mass - before.mass - mass_flux,
        momentum=(
            after.momentum[0] - before.momentum[0] - momentum_flux[0],
            after.momentum[1] - before.momentum[1] - momentum_flux[1],
        ),
        energy=after.energy - before.energy - energy_flux,
    )


def conservation_score(
    residual: ConservationState,
    mass_scale: float = 1.0,
    momentum_scale: float = 1.0,
    energy_scale: float = 1.0,
) -> float:
    """Convert normalized conservation residuals into a 0-100 audit score."""
    if min(mass_scale, momentum_scale, energy_scale) <= 0.0:
        raise ValueError("all normalization scales must be strictly positive")
    penalty = sqrt(
        (residual.mass / mass_scale) ** 2
        + (residual.momentum[0] / momentum_scale) ** 2
        + (residual.momentum[1] / momentum_scale) ** 2
        + (residual.energy / energy_scale) ** 2
    )
    return 100.0 / (1.0 + penalty)
