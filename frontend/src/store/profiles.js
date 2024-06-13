import { getProfilesRequest, addProfileRequest } from "@/connectors/profiles";

const initialState = {
  profiles: [],
  activeProfile: {},
};

const getters = {};
const mutations = {
  selectProfile(state, profile) {
    state.activeProfile = profile;
  },
  addProfiles(state, profiles) {
    state.profiles.push(...profiles);
  },
  clearProfiles(state) {
    state.profile = [];
  },
};
const actions = {
  async getProfiles({ commit }) {
    const res = await getProfilesRequest();

    if (!res) {
      return;
    }

    const newProfiles = res.data.results;
    commit("addProfiles", newProfiles);
  },
  async addProfile({ dispatch }, { title, pin }) {
    const profileObj = {
      title: title,
      pin: pin,
    };

    try {
      const res = await addProfileRequest(profileObj);

      if (!res) {
        return;
      }
    } catch (error) {
      dispatch("error/setError", error.message, { root: true });
    }

    dispatch("clearProfiles");
  },
};

export default {
  namespaced: true,
  state: initialState,
  getters,
  actions,
  mutations,
};
