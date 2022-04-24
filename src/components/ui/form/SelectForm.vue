<template>
  <LabelForm :idLabel="idLabel" :name="name">
    <select :id="idLabel" :value="modelValue" @change="changeOption">
      <slot />
      <option v-for="option in options" :key="option.id" :value="option.id">
        {{ option.name }}
      </option>
    </select>
  </LabelForm>
</template>

<script>
import LabelForm from "./LabelForm.vue";
export default {
  name: "SelectForm",
  props: {
    idLabel: {
      type: String,
      default: null,
    },
    name: {
      type: String,
      default: null,
    },
    modelValue: {
      type: String,
    },
    options: {
      type: Array,
      default: () => [],
    },
  },
  data() {
    return {};
  },
  components: { LabelForm },
  methods: {
    changeOption(event) {
      this.$emit("update:modelValue", event.target.value);
    },
  },
};
</script>

<style lang="scss" scoped>
@include grup-input();
</style>
