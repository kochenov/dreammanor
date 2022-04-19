<template>
  <div class="logo">
    <router-link to="/">
      <img src="@/assets/images/logo.png" alt="" />
    </router-link>
    <span>УСАДЬБА МЕЧТЫ</span>
  </div>
</template>

<script>
export default {
  name: "LogoHeader",
};
</script>

<style lang="scss" scoped>
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
</style>
