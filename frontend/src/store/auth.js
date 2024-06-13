import {
  loginRequest,
  signUpRequest,
  logoutRequest,
  sessionRequest,
} from "@/connectors/auth";
import router from "@/router";

const initialState = {
  authenticated: false,
};

const getters = {};
const mutations = {
  setAuthenticated(state, authenticated) {
    state.authenticated = authenticated;
  },
};
const actions = {
  async session({ commit }) {
    const res = await sessionRequest();
    if (!res) {
      return;
    }

    commit("setAuthenticated", true);
    router.push({ name: "home" });
  },
  async login({ dispatch }, data) {
    await dispatch("auth", [loginRequest, data]);
  },
  async signUp({ dispatch }, data) {
    await dispatch("auth", [signUpRequest, data]);
  },
  async auth({ dispatch, commit }, [authRequest, data]) {
    try {
      await authRequest(...data);
      commit("setAuthenticated", true);
      router.push({ name: "home" });
    } catch (error) {
      dispatch("error/setError", error.message, { root: true });
    }
  },
  async logout({ commit }) {
    const res = await logoutRequest();
    if (!res) {
      return;
    }

    commit("setAuthenticated", false);
    router.push({ name: "login" });
  },
};

export default {
  namespaced: true,
  state: initialState,
  getters,
  actions,
  mutations,
};
