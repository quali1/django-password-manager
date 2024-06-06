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

async function axiosRequest(method, subUrl, data) {
  return await axios({
    method: method,
    url: BASE_URL + subUrl,
    headers: {
      "Content-Type": "application/json",
    },
    data: JSON.stringify(data),
  });
}

function convertAxiosErrors(error) {
  if (error.response) {
    throw Error(parseErrorData(error.response.data));
  } else if (error.request) {
    throw Error("Responce error!");
  } else {
    throw Error("Request error!");
  }
}

export { convertAxiosErrors, axiosRequest };
