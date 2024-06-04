<template>
  <button class="button">
    <slot></slot>
  </button>
</template>

<style lang="scss" scoped>
.button {
  border-radius: $border-radius;
  border: none;
  text-align: center;
  transition: opacity $transition;

  &:hover {
    opacity: $hover-opacity;
  }
}
</style>
