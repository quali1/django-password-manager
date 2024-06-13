import {
  convertAxiosErrors,
  axiosGetRequest,
  axiosPostRequest,
} from "@/connectors/helpers";

async function getProfilesRequest() {
  try {
    return await axiosGetRequest("/api/profiles/");
  } catch (error) {
    convertAxiosErrors(error);
  }
}

async function addProfileRequest(id) {
  try {
    return await axiosPostRequest("/api/saved-passwords/", { id: id });
  } catch (error) {
    convertAxiosErrors(error);
  }
}

export { getProfilesRequest, addProfileRequest };
