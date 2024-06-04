<template>
  <div class="profiles">
    <div
      class="profile"
      :class="{
        active: profile.id == activeProfile.id,
      }"
      v-for="profile in profiles"
      :key="profile.id"
      @click="selectProfile(profile)"
    >
      <avatar-component class="avatar"></avatar-component>
      <span class="title">{{ profile.title.substring(0, 6) }}</span>
    </div>
    <div class="profile"><span class="title">Add Profile</span></div>
  </div>
</template>

<script>
import { mapState, mapMutations } from "vuex";

import AvatarComponent from "@/ui/components/AvatarComponent";

export default {
  components: {
    AvatarComponent,
  },
  computed: {
    ...mapState("profiles", ["profiles", "activeProfile"]),
  },
  methods: {
    ...mapMutations("profiles", ["selectProfile"]),
  },
};
</script>

<style lang="scss" scoped>
.profiles {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: $small-gap;
}

.profile {
  display: flex;
  flex-direction: column;
  align-items: center;
  background: $light-main-color;
  height: 80px;
  justify-content: center;
  border-radius: 8px;
  cursor: pointer;
  transition: opacity $transition, background $transition;

  &:hover {
    opacity: $hover-opacity;
  }

  &.active {
    background: $green-color;
  }
}

.avatar {
  width: 34px;
  height: 34px;
  margin-bottom: calc($gap / 2);
}

.title {
  font-size: 12px;
  letter-spacing: 1.8px;
  text-indent: 1.8px;
  font-weight: 300;
  text-align: center;
}
</style>
