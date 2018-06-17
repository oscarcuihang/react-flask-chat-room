const webpack = require('webpack');
const path = require('path');
const config = {
    entry:  __dirname + '/js/index.jsx',
    output: {
        path: __dirname + '/dist',
        filename: 'bundle.js',
    },
    resolve: {
        extensions: ['.js', '.jsx', '.css']
    },
    module: {
      rules: [
        {
          test: /\.jsx?/,
          exclude: /node_modules/,
          use: 'babel-loader'
        },
        {
          test: /\.css$/,
          loader: 'style-loader'
        },
        {
          test: /\.css$/,
          loader: 'css-loader'
        },
        {
          test: /\.(ttf|eot|svg|woff|woff2)(\?.+)?$/,
          loader: 'file-loader?name=[hash:12].[ext]'
        }
      ]
    },
};
module.exports = config;
