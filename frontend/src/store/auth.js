import {
  loginRequest,
  signUpRequest,
  logoutRequest,
  sessionRequest,
} from "@/connectors/auth";
import router from "@/router";

const initialState = {
  token: "",
};

const getters = {};
const mutations = {
  setToken(state, token) {
    state.token = token;
  },
};
const actions = {
  saveToken({ commit }, token) {
    localStorage.setItem("token", token);
    commit("setToken", token);
  },
  clearToken({ commit }) {
    localStorage.setItem("token", "");
    commit("setToken", "");
  },
  async session({ commit }) {
    const token = localStorage.getItem("token");
    if (token) {
      try {
        await sessionRequest(token);
        commit("setToken", token);
        router.push({ name: "home" });
      } catch {
        localStorage.setItem("token", "");
        router.push({ name: "login" });
      }
    }
  },
  async login({ dispatch }, data) {
    await dispatch("auth", [loginRequest, data]);
  },
  async signUp({ dispatch }, data) {
    await dispatch("auth", [signUpRequest, data]);
  },
  async auth({ dispatch }, [authRequest, data]) {
    try {
      const res = await authRequest(...data);
      dispatch("saveToken", res.data.token);
      router.push({ name: "home" });
    } catch (error) {
      dispatch("error/setError", error.message, { root: true });
    }
  },
  async logout({ dispatch, state }) {
    await logoutRequest(state.token);
    dispatch("clearToken");
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
