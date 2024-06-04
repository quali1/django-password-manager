<template>
  <div class="home">
    <home-sidebar></home-sidebar>
    <div class="container">
      <home-header></home-header>
      <div class="content">
        <div class="text">
          Keep<br />your password<br />
          save
        </div>
      </div>
    </div>
    <home-pop-up />
    <transition>
      <div class="sidebar-blur" v-if="sidebarActive"></div>
    </transition>
    <transition>
      <div class="pop-up-blur" v-if="popUpActive"></div>
    </transition>
  </div>
</template>

<script>
import { mapState } from "vuex";

import HomeSidebar from "@/ui/pages/Home/HomeSidebar";
import HomeHeader from "@/ui/pages/Home/HomeHeader";
import HomePopUp from "@/ui/pages/Home/HomePopUp";

export default {
  components: {
    HomeHeader,
    HomeSidebar,
    HomePopUp,
  },
  computed: {
    ...mapState("home", ["sidebarActive", "popUpActive"]),
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
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  padding: 0 calc($gap * 2);
}

.text {
  text-transform: uppercase;
  font-size: 36px;
  letter-spacing: 18px;
  line-height: 130%;
}

.sidebar-blur,
.pop-up-blur {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  backdrop-filter: blur($blur);
}

.sidebar-blur {
  display: none;
  z-index: $sidebar-blur-z-index;
}

.pop-up-blur {
  z-index: $pop-up-blur-z-index;
}

@media screen and (max-width: $hide-sidebar-width) {
  .sidebar-blur {
    display: block;
  }
}
</style>
