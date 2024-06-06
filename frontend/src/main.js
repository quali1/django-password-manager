import { createApp } from "vue";
import App from "@/ui/App";
import router from "@/router";
import store from "@/store";

router.beforeEach(async (to, from, next) => {
  store.dispatch("auth/session");
  if (to.meta.requiresAuth && !store.state.auth.token) {
    next({ name: "login" });
  }

  if (to.name === "login" && store.state.auth.token) {
    next({ name: "home" });
  } else next();
});

createApp(App).use(store).use(router).mount("#app");
