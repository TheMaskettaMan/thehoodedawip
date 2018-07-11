
const path = require('path')



module.exports = {
	mode: 'development',
	entry: './main.js',
	devtool: 'inline-source-map',
	context: path.resolve(__dirname, './masketta_code/js'),
	output: {
		filename: '[name].bundle.js',
		path: path.resolve(__dirname, './masketta_code/masketta_dist')
	},
	
	module: {
	// lint js, convert it from es6
	// load css/less through appropriate loaders
		rules: [
			{
				test: /\.js/,
				enforce: "pre",
				exclude: /node_modules/,
				loader: "eslint-loader"
			},
			{	
				test: /\.js$/,
				exclude: /(node_modules|bower_components)/,
				use: {
					loader: 'babel-loader',
					options: {
						presets: ['react', 'babel-preset-env']
					}
				}
			},
//			{ no current use of css files
//				test: /\.css$/,
//				use: [
//					{ loader: 'style-loader' },
//					{ loader: 'css-loader' },
//				]
//			},
			{
				test: /\.(png|svg|jpg|gif)$/,
				use: [
					{
						loader: 'file-loader',
						options : {
							name: '[name].[ext]',
							// TODO investigate [path] variable working with
							// name as written above
							outputPath: 'images/'
						}
					}
				]
			},
			{
				test: /\.less$/,
					use: [{
						loader: 'style-loader'
					},
					{
						loader: 'css-loader'
					}, 
					{
						loader: 'less-loader',
						options: {
							strictMath: true,
							noIeCompact: true,
						}	
					}
				]
			}
		]
	}
}


