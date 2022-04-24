<template>
  <form @submit.prevent="" action="" method="GET">
    <slot />
  </form>
</template>

<script>
export default {
  name: "FormGrid",
};
</script>

<style lang="scss" scoped>
form {
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: auto;
  gap: 30px;
}
</style>
