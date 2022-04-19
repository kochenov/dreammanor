<template>
  <header class="header">
    <div class="wrap">
      <div class="logo-wrap"><LogoHeader /></div>
      <div class="nav-wrap">
        <MainMenu />
      </div>
    </div>
  </header>
</template>
<script>
import MainMenu from "../block/navigation/MainMenu.vue";
import LogoHeader from "../block/logo/LogoHeader.vue";
export default { components: { MainMenu, LogoHeader } };
</script>
<style lang="scss" scoped>
.header {
  background: rgb(245, 250, 255);
  background: linear-gradient(
    90deg,
    rgba(245, 250, 255, 1) 50%,
    rgba(25, 68, 132, 1) 50%
  );
  background-size: 100% 80px;
  background-repeat: no-repeat;
  background-position-y: bottom;
  margin-bottom: 1px;

  .wrap {
    display: grid;
    grid-template-areas: "logo-wrap nav-wrap";
    grid-template-columns: 380px auto;
    grid-template-rows: 126px;
    @include screen-size(xl) {
      grid-template-columns: 200px auto;
    }
    @include screen-size(lg) {
      grid-template-areas: "nav-wrap";
      grid-template-columns: auto;
    }
  }

  .logo-wrap {
    grid-area: logo-wrap;
    @include screen-size(lg) {
      grid-area: none;
      display: none;
    }
  }

  .nav-wrap {
    grid-area: nav-wrap;
  }
}
</style>
