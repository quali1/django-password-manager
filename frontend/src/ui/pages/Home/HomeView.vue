<template>
  <div class="home">
    <home-sidebar></home-sidebar>
    <div class="container">
      <home-header></home-header>
      <div class="content">
        <router-view class="subpage" />
      </div>
    </div>
    <transition>
      <div class="sidebar-blur" v-if="sidebarActive"></div>
    </transition>
  </div>
</template>

<script>
import { mapState } from "vuex";

import HomeSidebar from "@/ui/pages/Home/HomeSidebar";
import HomeHeader from "@/ui/pages/Home/HomeHeader";

export default {
  components: {
    HomeHeader,
    HomeSidebar,
  },
  computed: {
    ...mapState("home", ["sidebarActive"]),
  },
};
</script>

<style lang="scss" scoped>
.home {
  display: flex;
  height: 100%;
  position: relative;
}

.container {
  width: 100%;
  display: flex;
  flex-direction: column;
}

.content {
  height: 100%;
  margin: 0 0 calc($gap * 2) calc($gap * 2);
  padding-right: calc($gap / 3 * 5);
  margin-right: calc($gap / 3);
  overflow-y: scroll;
}

.subpage {
  width: 100%;
  min-height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.sidebar-blur {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  backdrop-filter: blur($blur);
  display: none;
  z-index: $sidebar-blur-z-index;
}

@media screen and (max-width: $hide-sidebar-width) {
  .sidebar-blur {
    display: block;
  }
}
</style>
