const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: true,
  assetsDir: "static",

  productionSourceMap: false,

  css: {
    loaderOptions: {
      scss: {
        additionalData: `@import "~@/assets/variables.scss";`,
      },
    },
  },
});
