<template>
  <div class="textarea">
    <textarea
      class="field"
      :value="modelValue"
      :placeholder="placeholder"
      @input="$emit('update:modelValue', $event.target.value)"
    />
  </div>
</template>

<script>
export default {
  props: {
    modelValue: {
      type: String,
      required: true,
    },
    placeholder: {
      type: String,
    },
  },
};
</script>

<style lang="scss" scoped>
.textarea {
  display: flex;
  border-radius: $border-radius $border-radius 0 0;
  background: none;
  border: none;
  padding-left: $gap;
  padding-right: calc($gap / 3);
  resize: none;
}

.field {
  width: 100%;
  background: none;
  border: none;
  resize: none;
  padding-right: calc($gap / 3 * 2);
}
</style>
