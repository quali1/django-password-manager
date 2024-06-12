import {
  convertAxiosErrors,
  axiosPostRequest,
  axiosGetRequest,
} from "@/connectors/helpers";

async function logoutRequest() {
  try {
    return await axiosPostRequest("/api/auth/logout/", {});
  } catch (error) {
    convertAxiosErrors(error);
  }
}

async function sessionRequest() {
  try {
    return await axiosGetRequest("/api/auth/session/", {});
  } catch (error) {
    convertAxiosErrors(error);
  }
}

async function loginRequest(username, password) {
  try {
    return await axiosPostRequest("/api/auth/login/", {
      username: username,
      password: password,
    });
  } catch (error) {
    convertAxiosErrors(error);
  }
}

async function signUpRequest(username, email, password) {
  try {
    return await axiosPostRequest("/api/auth/signup/", {
      username: username,
      email: email,
      password: password,
    });
  } catch (error) {
    convertAxiosErrors(error);
  }
}

export { loginRequest, signUpRequest, logoutRequest, sessionRequest };
