import {
  getPasswordsRequest,
  addPasswordRequest,
} from "@/connectors/passwords";

const initialState = {
  passwords: [],
  activePassword: null,
  passwordsLoaded: false,
};

const getters = {};
const mutations = {
  selectPassword(state, password) {
    state.activePassword = password;
  },
  addPasswords(state, passwords) {
    state.passwords.push(...passwords);
  },
  clearPasswords(state) {
    state.passwords = [];
  },
  setPasswordsLoaded(state, value) {
    state.passwordsLoaded = value;
  },
};
const actions = {
  addPasswords({ commit }, passwords) {
    commit("addPasswords", passwords);
    commit("setPasswordsLoaded", false);
  },
  clearPasswords({ commit }) {
    commit("clearPasswords");
    commit("setPasswordsLoaded", false);
  },
  async getPasswords({ commit, dispatch, state, rootState }, limit) {
    const offset = state.passwords.length;
    const token = rootState.auth.token;
    const res = await getPasswordsRequest(limit, offset, token);

    const newPasswords = res.data.results;
    dispatch("addPasswords", newPasswords);

    if (!res.data.next) {
      commit("setPasswordsLoaded", true);
    }
  },
  async addPassword(
    { dispatch, rootState },
    { username, password, website = null, note = null, profile = null }
  ) {
    const token = rootState.auth.token;
    const passwordObj = {
      username: username,
      password: password,
      website: website,
      note: note,
      profile: profile,
    };
    const res = await addPasswordRequest(passwordObj, token);
    console.log(res);
    dispatch("clearPasswords");
  },
};

export default {
  namespaced: true,
  state: initialState,
  getters,
  actions,
  mutations,
};
