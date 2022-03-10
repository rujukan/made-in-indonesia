/** @type {import('next').NextConfig} */
// const nextConfig = {
//  reactStrictMode: true,
// }

// module.exports = nextConfig
//

// next.config.js
const isProd = process.env.NODE_ENV === 'production'

module.exports = {
  assetPrefix: isProd ? '/made-in-indonesia/' : ''
}
