<template>
  <div class="search">
    <input-component
      class="input"
      v-model="text"
      @keyup.enter="emitSearch"
      placeholder="Search..."
    />
  </div>
</template>

<script>
import InputComponent from "@/ui/components/InputComponent";

export default {
  components: {
    InputComponent,
  },
  data() {
    return {
      text: "",
    };
  },
  methods: {
    emitSearch() {
      this.$emit("search", this.text);
    },
  },
};
</script>

<style lang="scss" scoped>
.input {
  background: $gray-color;

  & > * {
    color: $black-color;
    font-size: 20px;
    letter-spacing: 3.6px;
  }
}
</style>
