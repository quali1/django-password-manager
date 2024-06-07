import { createApp } from "vue";
import App from "@/ui/App";
import router from "@/router";
import store from "@/store";

router.beforeEach(async (to, from, next) => {
  if (to.meta.requiresAuth && !store.state.auth.token) {
    next({ name: "login" });
  }

  if (to.meta.auth && store.state.auth.token) {
    next({ name: "home" });
  } else next();
});

createApp(App).use(store).use(router).mount("#app");
store.dispatch("auth/session");
