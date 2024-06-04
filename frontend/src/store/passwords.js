const initialState = {
  passwords: [
    { id: 1, title: "passwosd1" },
    { id: 2, title: "password2" },
    { id: 3, title: "password3" },
    { id: 4, title: "password4" },
    { id: 5, title: "password5" },
    { id: 6, title: "password6" },
    { id: 7, title: "password7" },
    { id: 8, title: "password8" },
    { id: 9, title: "password9" },
    { id: 10, title: "password10" },
    { id: 11, title: "password11" },
    { id: 12, title: "password12" },
    { id: 13, title: "password13" },
    { id: 14, title: "password14" },
    { id: 15, title: "password15" },
  ],
  activePassword: null,
};

const getters = {};
const mutations = {
  selectPassword(state, password) {
    state.activePassword = password;
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
