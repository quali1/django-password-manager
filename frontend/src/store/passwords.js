import {
  getPasswordsRequest,
  addPasswordRequest,
} from "@/connectors/passwords";

const initialState = {
  passwords: [],
  activePassword: null,
  passwordsLoaded: false,
  search: "",
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
  setSearch(state, search) {
    state.search = search;
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
  setSearch({ dispatch, commit }, search) {
    dispatch("clearPasswords");
    commit("setSearch", search);
  },
  async getPasswords({ commit, dispatch, state }, limit) {
    const offset = state.passwords.length;
    const res = await getPasswordsRequest(limit, offset, state.search);

    if (!res) {
      return;
    }

    const newPasswords = res.data.results;
    dispatch("addPasswords", newPasswords);

    if (!res.data.next) {
      commit("setPasswordsLoaded", true);
    }
  },
  async addPassword(
    { dispatch },
    { username, password, website = null, note = null, profile = null }
  ) {
    const passwordObj = {
      username: username,
      password: password,
      website: website,
      note: note,
      profile: profile,
    };

    try {
      const res = await addPasswordRequest(passwordObj);

      if (!res) {
        return;
      }
    } catch (error) {
      dispatch("error/setError", error.message, { root: true });
    }

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
