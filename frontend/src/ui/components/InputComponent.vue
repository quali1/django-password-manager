<template>
  <div class="input">
    <input
      class="field"
      :type="fieldType"
      :value="modelValue"
      :placeholder="placeholder"
      @input="$emit('update:modelValue', $event.target.value)"
    />
    <div v-if="hide" class="control">
      <span class="divider" />
      <button
        class="toggle"
        :class="{
          visible: isVisible,
        }"
        type="button"
        @click="toggleVisibility"
      >
        <img
          class="hide"
          src="@/assets/images/hide-pass.svg"
          alt="Hide password"
        />
        <img
          class="show"
          src="@/assets/images/show-pass.svg"
          alt="Show password"
        />
      </button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    modelValue: {
      type: String,
      required: true,
    },
    placeholder: {
      type: String,
    },
    hide: {
      type: Boolean,
    },
  },
  data() {
    return {
      isVisible: false,
    };
  },
  computed: {
    fieldType() {
      return this.isVisible || !this.hide ? "text" : "password";
    },
  },
  methods: {
    toggleVisibility() {
      this.isVisible = !this.isVisible;
    },
  },
};
</script>

<style lang="scss" scoped>
.input {
  display: flex;
  align-items: center;
  height: $elem-height;
  border-radius: $border-radius;
}

.field {
  flex: 1;
  background: none;
  border: none;
  padding: $elem-padding;
  height: 100%;
  width: 100%;
}

.control {
  display: flex;
  align-items: center;
  height: 100%;
}

.divider {
  width: 2px;
  height: 75%;
  border-radius: 1px;
  background: $light-main-color;
  vertical-align: middle;
}

.toggle {
  border: none;
  background: none;
  position: relative;
  height: 100%;
  transition: opacity $transition;
  padding: 0 calc($gap - 1px);
  display: flex;
  align-items: center;

  &:hover {
    opacity: $hover-opacity;
  }

  &.visible {
    .show {
      opacity: 0;
      position: absolute;
    }
  }

  &:not(.visible) {
    .hide {
      opacity: 0;
      position: absolute;
    }
  }
}

.show,
.hide {
  transition: $transition opacity;
  height: 48%;
}
</style>
