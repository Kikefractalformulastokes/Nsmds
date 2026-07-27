"""EGIL: auditable invariance and conservation gates for NS-MDS."""

from .core import (
    ConservationState,
    Frame2D,
    conservation_residual,
    conservation_score,
    frame_consistency_error,
)

__all__ = [
    "ConservationState",
    "Frame2D",
    "conservation_residual",
    "conservation_score",
    "frame_consistency_error",
]
