<template>
  <div>
    <header class="header">
      <div class="wrap header__wrap">
        <div class="header__logo-wrap">
          <div class="logo">
            <a class="logo-link" href="#">
              <img src="@assets/img/logo.png" alt="" />
            </a>
            <span>УСАДЬБА МЕЧТЫ</span>
          </div>
        </div>
        <div class="header__nav-wrap">
          <MainMenu />
        </div>
      </div>
    </header>

    <PromoLink />
    <Breadcrumbs />
    <router-view />
  </div>
</template>
<script>
import PromoLink from "@/components/main/PromoLink";
import Breadcrumbs from "@/components/main/Breadcrumbs";
import MainMenu from "@/components/block/navigation/MainMenu.vue";
export default {
  name: "IndexLayout",
  components: {
    PromoLink,
    Breadcrumbs,
    MainMenu,
  },
};
</script>
