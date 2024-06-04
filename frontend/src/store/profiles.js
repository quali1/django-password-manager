const initialState = {
  profiles: [
    { id: 1, title: "Work" },
    { id: 2, title: "Test" },
    { id: 3, title: "Prof" },
    { id: 4, title: "Stop" },
  ],
  activeProfile: { id: 2, title: "Test" },
};

const getters = {};
const mutations = {
  selectProfile(state, profile) {
    state.activeProfile = profile;
  },
};
const actions = {};

export default {
  namespaced: true,
  state: initialState,
  getters,
  actions,
  mutations,
};
