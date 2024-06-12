const initialState = {
  sidebarActive: true,
};

const getters = {};
const mutations = {
  toggleSidebar(state) {
    state.sidebarActive = !state.sidebarActive;
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
