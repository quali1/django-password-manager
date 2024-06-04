<template>
  <div class="passwords">
    <div
      class="password"
      v-for="password in passwords"
      :key="password.id"
      :class="{
        active: activePassword && password.id === activePassword.id,
      }"
      @click="selectPassword(password)"
    >
      <span class="text">{{ password.title }}</span>
    </div>
  </div>
</template>

<script>
import { mapState, mapMutations } from "vuex";

export default {
  computed: {
    ...mapState("passwords", ["passwords", "activePassword"]),
  },
  methods: {
    ...mapMutations("passwords", ["selectPassword"]),
  },
};
</script>

<style lang="scss" scoped>
.passwords {
  overflow-y: scroll;
  padding: 0 calc($gap / 3 * 2);
  margin: 0 calc($gap / 3);
}

.password {
  display: flex;
  align-items: center;
  height: $elem-height;
  width: 100%;
  border-radius: $border-radius;
  transition: background $fast-transition, opacity $transition;
  padding: $elem-padding;
  margin-bottom: calc($gap / 3);
  cursor: pointer;
  position: relative;

  &.active,
  &:hover {
    background: $light-main-color;
  }

  &:hover {
    opacity: $hover-opacity;
  }
}

.text {
  font-size: 15px;
  letter-spacing: 3px;
  overflow: hidden;
}
</style>
