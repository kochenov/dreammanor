<template>
  <LabelForm :idLabel="idLabel" :name="name">
    <input
      :value="modelValue"
      @input="updateInput"
      :id="idLabel"
      :type="typeInput"
      :min="min"
      :max="max"
      :placeholder="placeholder"
    />
  </LabelForm>
</template>

<script>
import LabelForm from "./LabelForm.vue";
export default {
  name: "InputForm",
  props: {
    idLabel: {
      type: String,
      default: null,
    },
    name: {
      type: String,
      default: null,
    },
    min: {
      type: String,
      default: "1",
    },
    max: {
      type: String,
      default: "1000",
    },
    modelValue: [String, Number],
    typeInput: { type: String, default: "text" },
    placeholder: { type: String },
  },
  components: { LabelForm },
  methods: {
    updateInput(event) {
      this.$emit("update:modelValue", event.target.value);
    },
  },
};
</script>

<style lang="scss" scoped>
@include grup-input();
</style>
