/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        forest: {
          50: '#f2f7f3',
          100: '#e1efe3',
          200: '#c3dfc9',
          300: '#95c4a3',
          400: '#61a377',
          500: '#3f8555',
          600: '#2f6a43',
          700: '#275537',
          800: '#23452f',
          900: '#1f3a29',
          950: '#0f2116',
        },
        river: {
          50: '#f0f9ff',
          100: '#e0f2fe',
          200: '#bae6fd',
          300: '#7dd3fc',
          400: '#38bdf8',
          500: '#0ea5e9',
          600: '#0284c7',
          700: '#0369a1',
          800: '#075985',
          900: '#0c4a6e',
        },
        earth: {
          50: '#faf8f5',
          100: '#f3f0e6',
          200: '#e6e0d0',
          300: '#d4c8ad',
          400: '#bea888',
          500: '#ac8f6c',
          600: '#9a7a5a',
          700: '#7f6249',
          800: '#68503f',
          900: '#554236',
          950: '#2e221b',
        }
      },
      fontFamily: {
        sans: ['Noto Sans', 'Noto Sans AZ', 'Inter', 'system-ui', 'sans-serif'],
      },
      animation: {
        'fade-in': 'fadeIn 0.5s ease-out',
        'slide-up': 'slideUp 0.6s ease-out',
        'scale-in': 'scaleIn 0.4s ease-out',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { opacity: '0', transform: 'translateY(20px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        scaleIn: {
          '0%': { opacity: '0', transform: 'scale(0.95)' },
          '100%': { opacity: '1', transform: 'scale(1)' },
        },
      },
    },
  },
  plugins: [],
};
