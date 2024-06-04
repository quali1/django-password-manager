<template>
  <div
    class="sidebar"
    :class="{
      active: sidebarActive,
    }"
  >
    <div class="container">
      <div class="control">
        <div class="search-block">
          <search-block />
          <burger-component :active="sidebarActive" @click="toggleSidebar" />
        </div>
        <icon-button-component class="button" @click="togglePopUp">
          <template #icon>
            <img src="@/assets/images/plus.svg" alt="Add" />
          </template>
          <template #text>
            <span class="button-text">Add new password</span>
          </template>
        </icon-button-component>
      </div>
      <home-passwords class="passwords" />
    </div>
  </div>
  <burger-component
    class="absolute-icon"
    :active="sidebarActive"
    @click="toggleSidebar"
  />
</template>

<script>
import { mapState, mapMutations } from "vuex";

import SearchBlock from "@/ui/blocks/SearchBlock";
import IconButtonComponent from "@/ui/components/IconButtonComponent";
import BurgerComponent from "@/ui/components/BurgerComponent";
import HomePasswords from "@/ui/pages/Home/HomePasswords";

export default {
  components: {
    SearchBlock,
    IconButtonComponent,
    HomePasswords,
    BurgerComponent,
  },
  computed: {
    ...mapState("home", ["sidebarActive"]),
  },
  methods: {
    ...mapMutations("home", ["toggleSidebar", "togglePopUp"]),
  },
};
</script>

<style lang="scss" scoped>
.sidebar {
  background: $dark-main-color;
  padding: calc($gap * 2) 0;
  max-width: $sidebar-max-width;
  width: 100%;
  transition: width $transition ease;
  overflow-y: hidden;
  z-index: $sidebar-z-index;

  &:not(.active) {
    width: 0;
  }
}

.container {
  display: flex;
  flex-direction: column;
  width: $sidebar-max-width;
  height: 100%;
}

.control {
  padding: 0 $gap;
}

.search-block {
  display: flex;
  gap: $gap;
}

.button {
  background: $light-main-color;
  height: $elem-height;
  width: 100%;
}

.passwords,
.button {
  margin-top: calc($gap * 2);
}

.passwords {
  max-height: 100%;
}

.absolute-icon {
  position: absolute;
  top: calc($gap * 2);
  left: calc($gap * 1.5);
}

.button-text {
  margin-left: 12px;
}

@media screen and (max-width: $hide-sidebar-width) {
  .sidebar {
    position: absolute;
    height: 100%;
  }
}
</style>
