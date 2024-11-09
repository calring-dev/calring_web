const path = require('path');

module.exports = {
  outputDir: path.resolve(__dirname, '../fast_api/dist'),
  assetsDir: 'static',
  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000'
      }
    }
  }
}