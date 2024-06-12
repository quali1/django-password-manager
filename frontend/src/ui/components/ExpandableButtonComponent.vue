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
        <img class="icon" src="@/assets/images/array.svg" alt="Array" />
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

.icon {
  font-weight: 300;
  position: absolute;
  color: $blue-color;
  transition: transform $transition, top $transition;
  transform: translateY(-50%) rotate(-90deg);
  height: 28%;
  top: 50%;
  right: 16px;
}

.active .icon {
  top: calc(50% + 1px);
  transform: translateY(-50%);
}
</style>
