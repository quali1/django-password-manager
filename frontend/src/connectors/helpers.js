import axios from "axios";

const BASE_URL = process.env.VUE_APP_BASEURL;

function parseErrorData(data) {
  const elem = Object.values(data)[0];
  if (typeof elem === Object) {
    return parseErrorData(elem);
  } else if (typeof elem === Array) {
    return elem[0];
  } else {
    return elem;
  }
}

async function axiosRequest({
  method,
  subUrl,
  headers = {},
  data = {},
  params = {},
}) {
  return await axios({
    method: method,
    url: BASE_URL + subUrl,
    headers: headers,
    data: data,
    params: params,
  });
}

async function axiosGetRequest(subUrl, params) {
  return await axiosRequest({
    method: "get",
    subUrl: subUrl,
    params: params,
  });
}

async function axiosPostRequest(subUrl, data) {
  const headers = {
    "Content-Type": "application/json",
  };

  return await axiosRequest({
    method: "post",
    subUrl: subUrl,
    headers: headers,
    data: data,
  });
}

function convertAxiosErrors(error) {
  // TODO: Catch problems with token -> logout
  if (error.response) {
    throw Error(parseErrorData(error.response.data));
  } else if (error.request) {
    throw Error("Responce error!");
  } else {
    throw Error("Request error!");
  }
}

export { convertAxiosErrors, axiosGetRequest, axiosPostRequest };
