const BundleTracker = require("webpack-bundle-tracker");

// Change this to match the path to your files in production (could be S3, CloudFront, etc.)
const DEPLOYMENT_PATH = "/static/dist/";

module.exports = {
  publicPath: process.env.NODE_ENV === "production" ? DEPLOYMENT_PATH : "http://localhost:8080/",
  outputDir: "static/dist",

  devServer: {
    public: "localhost:8080",
    headers: {
      "Access-Control-Allow-Origin": "*"
    },
  },

  configureWebpack: {
    plugins: [
      new BundleTracker({ path: __dirname, filename: "webpack-stats.json" })
    ]
  }
};
