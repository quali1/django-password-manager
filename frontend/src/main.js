import { createApp } from "vue";
import App from "@/ui/App";
import router from "@/router";
import store from "@/store";

router.beforeEach(async (to, from, next) => {
  store.dispatch("auth/getSession");
  if (to.meta.requiresAuth && !store.state.auth.authenticated) {
    next({ name: "login" });
  }

  if (to.name === "login" && store.state.auth.authenticated) {
    next({ name: "home" });
  } else next();
});

createApp(App).use(store).use(router).mount("#app");
