import {
  convertAxiosErrors,
  axiosGetRequest,
  axiosPostRequest,
} from "@/connectors/helpers";

async function getPasswordsRequest(limit, offset, token) {
  try {
    return await axiosGetRequest(
      "/api/saved-passwords/",
      {
        limit: limit,
        offset: offset,
      },
      token
    );
  } catch (error) {
    convertAxiosErrors(error);
  }
}

async function addPasswordRequest(passwordObj, token) {
  try {
    return await axiosPostRequest("/api/saved-passwords/", passwordObj, token);
  } catch (error) {
    convertAxiosErrors(error);
  }
}

export { getPasswordsRequest, addPasswordRequest };
