<template>
  <div
    class="expandable-button"
    :class="{
      active: active,
    }"
  >
    <icon-button-component class="button" @click="toggle">
      <template #icon>
        <slot name="icon"></slot>
      </template>
      <template #text>
        <slot name="text"></slot>
        <span class="icon">></span>
      </template>
    </icon-button-component>
    <div class="content-wrapper" ref="contentWrapper">
      <div class="content">
        <slot name="content"></slot>
      </div>
    </div>
  </div>
</template>

<script>
import IconButtonComponent from "@/ui/components/IconButtonComponent";

export default {
  components: {
    IconButtonComponent,
  },
  data() {
    return {
      active: false,
      contentHeight: null,
    };
  },
  methods: {
    toggle() {
      this.active = !this.active;
    },
  },
  mounted() {
    this.contentHeight = this.$refs.contentWrapper.scrollHeight + "px";
  },
};
</script>

<style lang="scss" scoped>
.expandable-button {
  border-radius: $border-radius;
  overflow: hidden;
  position: relative;

  &:not(.active) .content-wrapper {
    max-height: 0;
  }
}

.button {
  width: 100%;
  border-radius: 0;
}

.content-wrapper {
  max-height: v-bind(contentHeight);
  transition: max-height $fast-transition;
  overflow: hidden;
}

.content {
  padding: $small-gap;
}

.icon {
  right: calc($gap - 4px);
  top: 6.5px;
  font-weight: 300;
  position: absolute;
  font-size: 20px;
  color: $blue-color;
  transition: transform $fast-transition;
}

.active .icon {
  transform: rotate(90deg);
}
</style>
