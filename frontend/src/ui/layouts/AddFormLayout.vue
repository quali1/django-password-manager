<template>
  <div class="add-form">
    <div class="header">
      <back-component />
    </div>
    <div class="inputs">
      <slot name="inputs"></slot>
    </div>
    <div class="buttons">
      <slot name="buttons"></slot>
    </div>
    <div class="errors">
      <error-component />
    </div>
  </div>
</template>

<script>
import ErrorComponent from "@/ui/components/ErrorComponent";
import BackComponent from "@/ui/components/BackComponent";

export default {
  components: {
    ErrorComponent,
    BackComponent,
  },
};
</script>

<style lang="scss" scoped>
.add-form {
  display: flex;
  flex-direction: column;
  gap: 36px;
}

.header {
  width: 100%;
  max-width: 360px;
}

.inputs {
  display: flex;
  flex-direction: column;
  max-width: 360px;
  gap: 36px;
}

.buttons {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.buttons > * {
  width: 180px;
  background: $blue-color;
  font-size: 20px;
  height: $elem-height;
  letter-spacing: 5px;
  text-transform: uppercase;
}

.errors {
  margin: 0;
}
</style>
