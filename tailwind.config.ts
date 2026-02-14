import type { Config } from 'tailwindcss';

const config: Config = {
  content: ['./app/**/*.{ts,tsx}', './components/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        brand: '#0b3b5c',
        accent: '#ff7a00',
      },
    },
  },
  plugins: [],
};

export default config;
