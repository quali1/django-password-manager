const initialState = {
  authenticated: false,
  error: false,
  csrf: "",
};

const getters = {};
const mutations = {
  login(state) {
    state.authenticated = true;
  },
  logout(state) {
    state.authenticated = false;
  },
  singUp(state) {
    void state;
  },
};
const actions = {
  getSession({ commit }) {
    void commit;
  },
};

export default {
  namespaced: true,
  state: initialState,
  getters,
  actions,
  mutations,
};
