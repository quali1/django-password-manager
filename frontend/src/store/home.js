const initialState = {
  sidebarActive: true,
  popUpActive: false,
};

const getters = {};
const mutations = {
  toggleSidebar(state) {
    state.sidebarActive = !state.sidebarActive;
  },
  togglePopUp(state) {
    state.popUpActive = !state.popUpActive;
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
