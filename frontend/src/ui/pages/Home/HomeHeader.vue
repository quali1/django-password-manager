<template>
  <div class="header">
    <avatar-component class="avatar" @click="toggleProfile" />
  </div>
  <transition>
    <home-profile-modal v-if="profileActive" />
  </transition>
</template>

<script>
import HomeProfileModal from "@/ui/pages/Home/HomeProfileModal";
import AvatarComponent from "@/ui/components/AvatarComponent";

export default {
  components: {
    AvatarComponent,
    HomeProfileModal,
  },
  data() {
    return {
      profileActive: false,
    };
  },
  methods: {
    toggleProfile() {
      this.profileActive = !this.profileActive;
    },
  },
};
</script>

<style lang="scss" scoped>
.header {
  padding: calc($gap * 2);
  display: flex;
  justify-content: end;
}

.avatar {
  z-index: $avatar-z-index;
  width: $elem-height;
  height: $elem-height;
  transition: opacity $transition;

  &:hover {
    opacity: $hover-opacity;
  }
}
</style>
