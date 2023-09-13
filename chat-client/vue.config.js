// const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   transpileDependencies: true
// })

module.exports = {
  productionSourceMap: false,
  publicPath: process.env.NODE_ENV === "production" ? "/static/" : "/",
};
