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
          <input-component
            class="search"
            :modelValue="search"
            @update:modelValue="(value) => setSearch(value)"
            placeholder="Search..."
          />
          <burger-component :active="sidebarActive" @click="toggleSidebar" />
        </div>
        <icon-button-component class="button" @click="addPassword">
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
import { mapState, mapMutations, mapActions } from "vuex";

import IconButtonComponent from "@/ui/components/IconButtonComponent";
import BurgerComponent from "@/ui/components/BurgerComponent";
import InputComponent from "@/ui/components/InputComponent";
import HomePasswords from "@/ui/pages/Home/HomePasswords";

export default {
  components: {
    IconButtonComponent,
    InputComponent,
    HomePasswords,
    BurgerComponent,
  },
  computed: {
    ...mapState("home", ["sidebarActive"]),
    ...mapState("passwords", ["search"]),
  },
  methods: {
    ...mapMutations("home", ["toggleSidebar"]),
    ...mapActions("passwords", ["setSearch"]),
    addPassword() {
      this.$router.push({ name: "add-password" });
    },
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
  overflow: hidden;
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

.search {
  background: $gray-color;

  & > * {
    color: $black-color;
    font-size: 20px;
    letter-spacing: 3.6px;
  }
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
  margin-left: 14px;
}

@media screen and (max-width: $hide-sidebar-width) {
  .sidebar {
    position: absolute;
    height: 100%;
  }
}
</style>
