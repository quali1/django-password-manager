import { createApp } from "vue";
import App from "@/ui/App";
import router from "@/router";
import store from "@/store";
import axios from "axios";

axios.defaults.withCredentials = true;

router.beforeEach(async (to, from, next) => {
  const authenticated = store.state.auth.authenticated;

  if (to.meta.requiresAuth && !authenticated) {
    next({ name: "login" });
  } else if (to.meta.auth && authenticated) {
    next({ name: "home" });
  } else next();
});

createApp(App).use(store).use(router).mount("#app");
store.dispatch("auth/session");
