<template>
  <div class="back" @click="back">
    <img class="icon" src="@/assets/images/array.svg" alt="Array" />
  </div>
</template>

<script>
export default {
  methods: {
    back() {
      this.$router.go(-1);
    },
  },
};
</script>

<style lang="scss" scoped>
.icon {
  width: 26px;
  transform: rotate(90deg);
  padding: 0 0 5px 0;
  transition: transform $transition, padding $transition;
  cursor: pointer;
}

.icon:hover {
  padding: 5px 0 0 0;
  opacity: $hover-opacity;
}
</style>
