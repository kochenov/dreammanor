<template>
  <div v-if="messages.length > 0">
    <div
      class="flesh"
      :class="[type, dop]"
      v-for="(message, index) in messages"
      :key="index"
    >
      {{
        type === "info"
          ? "Информация"
          : type === "alert"
          ? "Придупреждение"
          : "Ошибка"
      }}: {{ message }}
    </div>
  </div>
</template>

<script>
export default {
  name: "FlashMessages",

  props: {
    messages: {
      type: Array,
      default: () => {},
    },
    type: {
      type: String,
      default: "error",
    },
    dop: {
      type: String,
    },
  },
};
</script>

<style lang="scss" scoped>
.flesh {
  padding: 15px 30px;
  border-radius: 3px;
  background-color: #fff;
  margin-bottom: 15px;
}
.error {
  color: red;
  border: 1px solid red;
}
.info {
  color: rgb(0, 132, 255);
  border: 1px solid rgb(0, 132, 255);
}
.aletr {
  color: rgb(220, 170, 30);
  border: 1px solid rgb(220, 170, 30);
}
.lite {
  border: none;
  padding: 0px 0px;
  margin-bottom: 5px;
}
</style>
