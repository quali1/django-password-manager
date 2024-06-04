<template>
  <button class="button">
    <slot name="icon"></slot>
    <div class="text">
      <slot name="text"></slot>
    </div>
  </button>
</template>

<style lang="scss" scoped>
.button {
  display: flex;
  align-items: center;
  padding: $elem-padding;
  border-radius: $border-radius;
  border: none;
  transition: opacity $transition;

  &:hover {
    opacity: $hover-opacity;
  }
}

.text {
  letter-spacing: 3px;
  text-indent: 3px;
  font-size: 15px;
}
</style>
