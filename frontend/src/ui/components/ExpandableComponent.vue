<template>
  <div
    class="expandable"
    :class="{
      active: active,
    }"
    ref="wrapper"
  >
    <slot></slot>
  </div>
</template>

<script>
export default {
  data() {
    return {
      contentHeight: null,
    };
  },
  props: {
    active: {
      type: Boolean,
    },
  },
  methods: {
    updateHeight() {
      this.contentHeight = this.$refs.wrapper.scrollHeight + "px";
    },
  },
  watch: {
    active() {
      this.updateHeight();
    },
  },
  mounted() {
    this.updateHeight();
  },
};
</script>

<style lang="scss" scoped>
.expandable {
  overflow: hidden;
  opacity: 1;
  transition: max-height $transition, opacity $transition;
  max-height: v-bind(contentHeight);

  &:not(.active) {
    max-height: 0;
  }
}
</style>
