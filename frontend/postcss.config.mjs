/** @type {import('postcss-load-config').Config} */
const config = {
  plugins: {
    '@tailwindcss/postcss': {}, // 최신 Next.js는 이 플러그인을 권장해
  },
};

export default config;