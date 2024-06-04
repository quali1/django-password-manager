<template>
  <div
    class="icon"
    :class="{
      active: active,
    }"
  >
    <span></span>
    <span></span>
    <span></span>
  </div>
</template>

<script>
export default {
  props: {
    active: {
      type: Boolean,
    },
  },
};
</script>

<style lang="scss" scoped>
.icon {
  display: inline-flex;
  flex-direction: column;
  justify-content: center;
  height: $elem-height;
  cursor: pointer;
  padding: $small-gap;
  border-radius: $border-radius;
  transition: background $transition, opacity $transition;

  &:hover,
  &.active {
    background: $light-main-color;
  }

  &:hover {
    opacity: $hover-opacity;
  }

  & span {
    display: block;
    width: 35px;
    height: 4px;
    margin: 4px 0;
    background-color: $dark-text-color;
    border-radius: 2px;
  }
}
</style>
