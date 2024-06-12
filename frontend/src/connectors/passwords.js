import {
  convertAxiosErrors,
  axiosGetRequest,
  axiosPostRequest,
} from "@/connectors/helpers";

async function getPasswordsRequest(limit, offset) {
  try {
    return await axiosGetRequest("/api/saved-passwords/", {
      limit: limit,
      offset: offset,
    });
  } catch (error) {
    convertAxiosErrors(error);
  }
}

async function addPasswordRequest(passwordObj) {
  try {
    return await axiosPostRequest("/api/saved-passwords/", passwordObj);
  } catch (error) {
    convertAxiosErrors(error);
  }
}

export { getPasswordsRequest, addPasswordRequest };
