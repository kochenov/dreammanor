<template>
  <header class="header">
    <div class="wrap">
      <div class="logo-wrap">
        <div class="logo">
          <router-link to="/">
            <img src="@/assets/images/logo.png" alt="" />
          </router-link>
          <span>УСАДЬБА МЕЧТЫ</span>
        </div>
      </div>
      <div class="nav-wrap">
        <MainMenu />
      </div>
    </div>
  </header>
</template>
<script>
import MainMenu from "../block/navigation/MainMenu.vue";
export default { components: { MainMenu } };
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

  // Логотип
  .logo {
    background-color: $top-header-background;
    padding-top: 16px;
    font-weight: 600;
    height: 100%;
    width: 100%;

    a {
      display: block;
      margin: 0 auto;
      height: 84px;
      max-width: 180px;

      img {
        width: 100%;
        height: 100%;
        object-fit: cover;
      }
    }

    span {
      text-align: center;
      display: block;
      padding-bottom: 10px;
    }
  }

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
