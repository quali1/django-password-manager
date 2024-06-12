const initialState = {
  isError: false,
  timeouts: [],
  error: "",
};

const getters = {};
const mutations = {
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
