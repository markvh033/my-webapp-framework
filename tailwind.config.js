/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./frontend/static/templates/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
],
darkMode: 'false'
}
