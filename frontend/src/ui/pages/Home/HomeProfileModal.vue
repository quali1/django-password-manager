<template>
  <div class="profile-modal">
    <div class="header">
      <div class="control">
        <div class="current">Current profile: {{ activeProfile.title }}</div>
        <button-component class="logout" @click="logout">
          Logout
        </button-component>
      </div>
    </div>
    <expandable-button-component class="profiles-button">
      <template #icon>
        <span class="button-img">
          <img src="@/assets/images/profile.svg" alt="Profiles" />
        </span>
      </template>
      <template #text>
        <span class="button-text">Profiles</span>
      </template>
      <template #content>
        <home-profiles />
      </template>
    </expandable-button-component>
    <icon-button-component class="settings">
      <template #icon>
        <span class="button-img">
          <img src="@/assets/images/settings.svg" alt="Settings" />
        </span>
      </template>
      <template #text>
        <span class="button-text">Settings</span>
      </template>
    </icon-button-component>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";

import HomeProfiles from "@/ui/pages/Home/HomeProfiles";
import ButtonComponent from "@/ui/components/ButtonComponent";
import IconButtonComponent from "@/ui/components/IconButtonComponent";
import ExpandableButtonComponent from "@/ui/components/ExpandableButtonComponent";

export default {
  components: {
    ButtonComponent,
    IconButtonComponent,
    ExpandableButtonComponent,
    HomeProfiles,
  },
  methods: {
    ...mapActions("auth", ["logout"]),
  },
  computed: {
    ...mapState("profiles", ["profiles", "activeProfile"]),
  },
};
</script>

<style lang="scss" scoped>
.profile-modal {
  position: absolute;
  top: calc($gap * 2 - $small-gap);
  right: calc($gap * 2 - $small-gap);
  z-index: $modal-z-index;
  padding: $small-gap;
  background: $light-main-color;
  border-radius: calc($border-radius * 1.5);
  font-weight: 400;
  display: flex;
  flex-direction: column;
  gap: $small-gap;
  width: 250px;
}

.control {
  margin-right: calc($small-gap + $elem-height);
  height: $elem-height;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.current {
  font-size: 10px;
  letter-spacing: 2.1px;
  text-indent: 2.1px;
  text-align: center;
  color: $purple-color;
  margin-top: 2px;
}

.logout,
.settings {
  height: $small-elem-height;
  letter-spacing: 3.8px;
  background: $main-color;
  font-weight: 400;
}

.profiles-button > * {
  background: $main-color;

  &:nth-child(1) {
    height: $small-elem-height;
    font-weight: 400;
  }
  &:nth-child(2) > * {
    padding: $small-gap;
  }
}

.logout {
  color: $red-color;
  text-transform: uppercase;
  text-indent: 3.8px;
}

.button-text {
  margin-left: 13px;
  color: $blue-color;
}

.button-img {
  width: 20px;
  display: flex;
  justify-content: center;
}

.settings {
  background: $main-color;
  width: 100%;
}
</style>
