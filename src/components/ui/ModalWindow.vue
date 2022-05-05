<template>
  <div class="dialog" v-if="show">
    <div class="content">
      <h3 v-if="name">{{ name }}</h3>
      <slot />
    </div>
  </div>
</template>

<script>
export default {
  name: "ModalWindow",
  props: {
    show: {
      type: Boolean,
      default: false,
    },
    name: {
      type: String,
    },
  },
};
</script>

<style lang="scss" scoped>
.dialog {
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background: #0000004b;
  position: fixed;
  display: flex;
}
.content {
  margin: auto;
  background: white;
  border-radius: 8px;
  padding: 25px 25px 10px 25px;
  @include screen-size(sm) {
    margin-left: 20px;
    margin-right: 20px;
  }

  h3 {
    font-size: 18rem;
    padding: 5px 0 15px 0;
    text-align: center;
    border-bottom: 1px solid #0000001f;
    margin-bottom: 20px;
  }
}
</style>
