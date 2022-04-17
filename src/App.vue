<template>
  <component :is="layout">
    <router-view />
  </component>
</template>
<style lang="scss">
@import "assets/style.scss";
</style>
<script>
import IndexLayout from "@/layouts/IndexLayout";
export default {
  components: {
    IndexLayout,
  },
  computed: {
    layout() {
      return this.$route.meta.layout + "-layout";
    },
  },
};
</script>
