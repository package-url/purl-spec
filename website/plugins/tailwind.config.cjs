/** @type {import('tailwindcss').Config} */
const defaultTheme = require('tailwindcss/defaultTheme');

export function tailwindPlugin(context, options) {
  return {
    name: 'tailwind-plugin',
    configurePostCss(postcssOptions) {
      postcssOptions.plugins = [
        require('postcss-import'),
        require('tailwindcss'),
        require('autoprefixer'),
      ];
      return postcssOptions;
    },
  };
}

module.exports = tailwindPlugin;

module.exports = {
	content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
	theme: {
		extend: {
			colors: {
				'primary-purple': '#3439AF',
				'primary-purple-light': '#C2C3E7',
				'primary-purple-deep': '#1A1D56',
				'primary-magenta': '#88267D',
				'primary-magenta-deep': '#4E1647',
				'primary-red': '#E83452',
				'legacy-cyclonedx': '#4CA7F1',
				'primary-active': '#2F78B5',
				'hyperlink': '#2157C4',
				black: '#191E22',
				grey: {
					50: '#F3F4F6',
					100: '#E6E6E6',
					200: '#D3D5D6',
					300: '#BDBDBD',
					400: '#A8ABAD',
					600: '#51575C',
					700: '#374151',
					800: '#3B4248',
					850: '#31383E',
					900: '#252D33',
				},
				gray: {
					50: '#F3F4F6',
					100: '#E6E6E6',
					200: '#D3D5D6',
					300: '#BDBDBD',
					400: '#A8ABAD',
					600: '#51575C',
					700: '#374151',
					800: '#3B4248',
					850: '#31383E',
					900: '#252D33',
				},
			},
			fontFamily: {
				sans: ['Poppins', 'sans-serif']
			},
			fontSize: {
				base: '12pt',
				'2xs': ['0.75rem', { lineHeight: '1rem' }],
				'xs': ['0.825rem', { lineHeight: '1rem' }],
				'sm': ['0.925rem', { lineHeight: '1.25rem' }],
				'lg': ['1.125rem', { lineHeight: '1.75rem' }],
				'xl': ['1.25rem', { lineHeight: '1.75rem' }],
				'2xl': ['1.5rem', { lineHeight: '2rem' }],
				'3xl': ['1.875rem', { lineHeight: '2.25rem' }],
				'4xl': ['2.25rem', { lineHeight: '2.5rem' }],
				'5xl': ['3rem', { lineHeight: '1' }],
				'6xl': ['3.75rem', { lineHeight: '1' }],
				'7xl': ['4.5rem', { lineHeight: '1' }],
				'8xl': ['6rem', { lineHeight: '1' }],
				'9xl': ['8rem', { lineHeight: '1' }],

				'h1': ['40pt', { lineHeight: '1.2' }],
				'h2': ['24pt', { lineHeight: '1.2' }],
				'h3': ['18pt', { lineHeight: '1.2' }],
				'h4': ['14pt', { lineHeight: '1.2' }],
				'label': ['14pt', { lineHeight: '1.2' }],
			},
			fontWeight: {
				'thin': 100,
				'lighter': 200,
				'light': 300,
				'normal': 400,
				'medium': 500,
				'semibold': 600,
				'bold': 700,
				'extrabold': 800,
				'black': 900,
				'h1': '500',  // Medium
				'h2': '500',  // Medium
				'h3': '400',  // Normal
				'h4': '600',  // Semi-Bold
				'label': '600'  // Semi-Bold
			},
			backgroundImage: {
				'primary-gradient': 'linear-gradient(269.12deg, rgba(232, 52, 82, 1) 0%, rgba(136, 38, 125, 1) 51.26%, rgba(52, 57, 175, 1) 100%)'
			},
		},
		screens: {
			sm: '640px',
			md: '768px',
			lg: '1024px',
			xl: '1280px',
			'2xl': '1536px',
		},
	},
	safelist: [
		'grid-cols-1',
		'grid-cols-2',
		'grid-cols-3',
		'grid-cols-4',
		'sm:grid-cols-1',
		'sm:grid-cols-2',
		'md:grid-cols-1',
		'md:grid-cols-2',
		'md:grid-cols-3',
		'md:grid-cols-4',
		'lg:grid-cols-1',
		'lg:grid-cols-2',
		'lg:grid-cols-3',
		'lg:grid-cols-4',
	],
	plugins: [
		require("@tailwindcss/typography"),
		require("@tailwindcss/forms"),
		require('@tailwindcss/aspect-ratio'),
		function ({ addBase, theme }) {
			addBase({
				':root': {
					'--color-grey-50': theme('colors.grey.50'),
					'--color-grey-100': theme('colors.grey.100'),
					'--color-grey-200': theme('colors.grey.200'),
					'--color-grey-400': theme('colors.grey.400'),
					'--color-grey-600': theme('colors.grey.600'),
					'--color-grey-700': theme('colors.grey.700'),
					'--color-grey-800': theme('colors.grey.800'),
					'--color-grey-850': theme('colors.grey.850'),
					'--color-grey-900': theme('colors.grey.900'),
					'--color-primary-purple': theme('colors.primary-purple'),
					'--color-primary-purple-light': theme('colors.primary-purple-light'),
					'--color=primary-purple-deep': theme('colors.primary-purple-deep'),
					'--color-primary-magenta': theme('colors.primary-magenta'),
					'--color-primary-magenta-deep': theme('colors.primary-magenta-deep'),
					'--color-primary-red': theme('colors.primary-red'),
					'--color-legacy-cyclonedx': theme('colors.legacy-cyclonedx'),
					'--color-primary-active': theme('colors.primary-active'),
					'--color-hyperlink': theme('colors.hyperlink'),
					'--color-black': theme('colors.black'),


					// EXPERIMENTAL
					'--ac-transparent': 'transparent',
					'--ac-white': '255, 255, 255',
					'--ac-primary': theme('colors.primary-magenta'),
					'--ac-secondary': '98, 251, 213',
					'--ac-dark': '22, 22, 22',
					'--ac-gray-100': '232, 232, 232',
					'--ac-gray-200': '185, 185, 185',
					'--ac-gray-300': '139, 139, 139',
					'--ac-gray-400': '92, 92, 92',
					'--ac-gray-500': '45, 45, 45',
					'--ac-success': '0, 255, 0',
					'--ac-warning': '255, 255, 0',
					'--ac-danger': '255, 0, 0'
				},
			});
		},
		function ({ addUtilities, theme }) {
			addUtilities({
				'.text-hyperlink': {
					color: theme('colors.hyperlink'),
					textDecoration: 'underline',
				},
			});
		},
	],
}
