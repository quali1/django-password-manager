import { createStore } from "vuex";

import auth from "@/store/auth";
import home from "@/store/home";
import passwords from "@/store/passwords";
import profiles from "@/store/profiles";

const debug = process.env.NODE_ENV !== "production";

export default createStore({
  modules: {
    auth,
    home,
    passwords,
    profiles,
  },
  strict: debug,
});
