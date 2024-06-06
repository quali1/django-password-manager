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
    <expandable-component :active="active">
      <div class="content"><slot name="content"></slot></div>
    </expandable-component>
  </div>
</template>

<script>
import IconButtonComponent from "@/ui/components/IconButtonComponent";
import ExpandableComponent from "@/ui/components/ExpandableComponent";

export default {
  components: {
    IconButtonComponent,
    ExpandableComponent,
  },
  data() {
    return {
      active: false,
    };
  },
  methods: {
    toggle() {
      this.active = !this.active;
    },
  },
};
</script>

<style lang="scss" scoped>
.expandable-button {
  border-radius: $border-radius;
  overflow: hidden;
  position: relative;
}

.button {
  width: 100%;
  border-radius: 0;
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
  transition: transform $transition;
}

.active .icon {
  transform: rotate(90deg);
}
</style>
