<template>
  <div>
    <HeaderPart />

    <PromoLink />
    <BreadcrumbsNav />
    <router-view />
  </div>
</template>
<script>
import PromoLink from "@/components/parts/PromoLink.vue";
import BreadcrumbsNav from "@/components/parts/BreadcrumbsNav.vue";
import HeaderPart from "@/components/parts/HeaderPart.vue";

export default {
  name: "IndexLayout",
  components: {
    PromoLink,
    BreadcrumbsNav,
    HeaderPart,
  },
};
</script>
<style lang="scss">
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

@import url("https://fonts.googleapis.com/css2?family=Bitter:ital,wght@0,200;0,300;0,400;0,600;0,800;1,300;1,500&display=swap");

html {
  font-size: 1px;
}

body {
  font-family: $font-text;
  background-color: $top-header-background;
  font-size: 14rem;
}
</style>
