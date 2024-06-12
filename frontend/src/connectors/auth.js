import { convertAxiosErrors, axiosPostRequest } from "@/connectors/helpers";

async function logoutRequest(token) {
  try {
    return await axiosPostRequest("/api/auth/logout/", {}, token);
  } catch (error) {
    convertAxiosErrors(error);
  }
}

async function sessionRequest(token) {
  try {
    return await axiosPostRequest("/api/auth/session/", {}, token);
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
