const HtmlWebPackPlugin = require( 'html-webpack-plugin' );

const path = require( 'path' );
module.exports = {
  context: __dirname,
  entry: './src/index.jsx',
  output: {
    path: path.resolve( __dirname, 'dist' ),
    filename: 'bundle.js',
    publicPath: '/',
  },
  watch: true,
  devServer: {
    historyApiFallback: true
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: [
              '@babel/preset-env',
              {
                plugins: [
                  '@babel/plugin-proposal-class-properties'
                ]
              }
            ]
          },
        }
      },
      {
        test: /\.css$/,
        use: [
          'style-loader',
          {
            loader: 'css-loader',
            options: {
              modules: true,
            }
          },
        ],
      },
      {
        test: /\.(png|j?g|svg|gif)?$/,
        use: 'file-loader'
      }
    ]
  },
  plugins: [
    new HtmlWebPackPlugin({
      template: path.resolve( __dirname, '../api/index.html' ),
      filename: 'index.html',
      favicon: './public/favicon.ico'
    }),
  ],
};
