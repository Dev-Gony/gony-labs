/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/**/*.{js,ts,jsx,tsx,mdx}", // 혹시 몰라서 추가
  ],
  theme: {
    extend: {
      colors: {
        background: "#030712",
        foreground: "#f9fafb",
        primary: {
          DEFAULT: "#3b82f6",
          dark: "#1d4ed8",
        },
        accent: "#8b5cf6",
      },
    },
  },
  plugins: [],
};