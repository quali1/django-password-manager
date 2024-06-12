<template>
  <div class="passwords" ref="passwords">
    <div
      class="password"
      v-for="password in passwords"
      :key="password.id"
      :class="{
        active: activePassword && password.id === activePassword.id,
      }"
      @click="selectPassword(password)"
    >
      <span class="text">{{ password.website }}</span>
    </div>
    <div class="observer" ref="observer"></div>
  </div>
</template>

<script>
import { mapState, mapMutations, mapActions } from "vuex";

export default {
  data() {
    return {
      passwordsHeight: 0,
      passwordHeight: 55,
    };
  },
  computed: {
    ...mapState("passwords", [
      "passwords",
      "activePassword",
      "passwordsLoaded",
    ]),
    passwordHeightPx() {
      return this.passwordHeight + "px";
    },
    passwordsLimit() {
      return Math.floor(this.contentHeight / this.passwordHeight);
    },
  },
  methods: {
    ...mapMutations("passwords", ["selectPassword"]),
    ...mapActions("passwords", ["getPasswords"]),
    updateHeight() {
      this.contentHeight = this.$refs.passwords.scrollHeight;
    },
  },
  mounted() {
    this.updateHeight();

    this.getPasswords(this.passwordsLimit * 2);

    const callback = (entries) => {
      if (!this.passwordsLoaded) {
        entries[0].isIntersecting && this.getPasswords(this.passwordsLimit);
      }
    };

    const observer = new IntersectionObserver(callback, {
      threshold: 0,
    });
    observer.observe(this.$refs.observer);
  },
  watch: {
    passwords: {
      handler(val) {
        console.log(val.length);
        if (!val.length) {
          this.getPasswords(this.passwordsLimit * 2);
        }
      },
      deep: true,
    },
  },
};
</script>

<style lang="scss" scoped>
.passwords {
  overflow-y: scroll;
  padding: 0 calc($gap / 3 * 2);
  margin: 0 calc($gap / 3);
  height: 100%;
}

.password {
  display: flex;
  align-items: center;
  height: v-bind(passwordHeightPx);
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

.observer {
  transform: translateY(-100px);
}
</style>
