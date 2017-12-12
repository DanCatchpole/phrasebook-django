var webpack = require('webpack');
var path = require('path');

var BUILD_DIR = path.resolve(__dirname, 'prod');
var APP_DIR = path.resolve(__dirname, 'dev');

var config = {
  entry: APP_DIR + '/app.jsx',
  output: {
    path: BUILD_DIR,
    filename: 'bundle.js'
  }
};

module.exports = config;
