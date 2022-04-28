<template>
  <div class="btn-group">
    <slot />
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.btn-group {
  margin: 10px 0;
  display: flex;
  justify-content: center;
  @include screen-size(sm) {
    flex-wrap: wrap;
  }
  gap: 20px;
}
</style>
