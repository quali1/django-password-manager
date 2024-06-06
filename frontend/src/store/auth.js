import {
  loginRequest,
  signUpRequest,
  logoutRequest,
  sessionRequest,
} from "@/connectors/auth";
import router from "@/router";

const initialState = {
  isError: false,
  timeouts: [],
  error: "",
  token: "",
};

const getters = {};
const mutations = {
  setToken(state, token) {
    state.token = token;
  },
  setError(state, message) {
    state.error = message;
  },
  setIsError(state, isError) {
    state.isError = isError;
  },
  setTimeouts(state, timeouts) {
    state.timeouts = timeouts;
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
      } catch {
        localStorage.setItem("token", "");
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
      dispatch("setError", error.message);
    }
  },
  async logout({ dispatch, state }) {
    await logoutRequest(state.token);
    dispatch("clearToken");
    router.push({ name: "login" });
  },
  setError({ dispatch, commit }, message) {
    dispatch("clearError");

    commit("setError", message);
    commit("setIsError", !!message);

    const t1 = setTimeout(() => {
      commit("setIsError", false);
    }, 4000);
    const t2 = setTimeout(() => {
      commit("setError", "");
    }, 4000 + 1000);
    commit("setTimeouts", [t1, t2]);
  },
  clearError({ commit, state }) {
    commit("setError", "");
    commit("setIsError", false);
    state.timeouts.forEach((id) => clearTimeout(id));
    commit("setTimeouts", []);
  },
};

export default {
  namespaced: true,
  state: initialState,
  getters,
  actions,
  mutations,
};
