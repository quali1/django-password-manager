<template>
  <transition>
    <div class="pop-up" v-if="active">
      <div class="container">
        <slot name="content"></slot>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  props: {
    active: {
      type: Boolean,
      required: true,
    },
  },
};
</script>

<style lang="scss" scoped>
.pop-up {
  position: absolute;
  width: 100%;
  top: 50%;
  transform: translateY(-50%);
  z-index: $pop-up-z-index;
  padding: $gap;
}

.container {
  margin: 0 auto;
}
</style>
