import { convertAxiosErrors, axiosRequest } from "@/connectors/helpers";

async function logoutRequest(token) {
  try {
    void token;
    // return await axiosRequest("POST", "/api/auth/login/", {
    //   username: username,
    //   password: password,
    // });
  } catch (error) {
    convertAxiosErrors(error);
  }
}

async function sessionRequest(token) {
  try {
    void token;
    // return await axiosRequest("POST", "/api/auth/login/", {
    //   username: username,
    //   password: password,
    // });
  } catch (error) {
    convertAxiosErrors(error);
  }
}

async function loginRequest(username, password) {
  try {
    return await axiosRequest("POST", "/api/auth/login/", {
      username: username,
      password: password,
    });
  } catch (error) {
    convertAxiosErrors(error);
  }
}

async function signUpRequest(username, email, password) {
  try {
    return await axiosRequest("POST", "/api/auth/signup/", {
      username: username,
      email: email,
      password: password,
    });
  } catch (error) {
    convertAxiosErrors(error);
  }
}

export { loginRequest, signUpRequest, logoutRequest, sessionRequest };
