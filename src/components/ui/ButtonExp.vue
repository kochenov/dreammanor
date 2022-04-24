<template>
  <button class="btn" :class="buttonType">
    <slot />
  </button>
</template>

<script>
export default {
  name: "ButtonExp",
  props: {
    buttonType: {
      type: String,
      default: () => {
        return "";
      },
    },
  },
};
</script>

<style lang="scss" scoped>
.btn {
  display: inline-block;
  padding: 12px 80px;
  //margin: 10px auto;
  font-size: 11px;
  font-weight: 600;
  text-transform: uppercase;
  color: white;
  border: none;
  background: #06b25f;
  border-radius: 3px;
  box-shadow: 0px 5px 19px 0px rgba(0, 2, 0, 0.21);
  transition: 0.5s ease;
  cursor: pointer;
  &:hover {
    background: #17696a;
    transition: 0.6s ease;
    color: white;
  }
}
.btn-outline {
  padding: 8px 10px;
  background: none;
  border: 2px solid #06b25f;
  color: #06b25f;
  box-shadow: none;
  &:hover {
    color: white;
    border-color: #17696a;
  }
}
.close {
  color: rgb(235, 135, 135) !important;
  border-color: rgb(235, 135, 135) !important;
  &:hover {
    color: white !important;
    background: rgb(235, 135, 135) !important;
    border-color: rgb(235, 135, 135) !important;
  }
}
</style>
