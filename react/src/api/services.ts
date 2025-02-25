import axios, {AxiosResponse} from "axios";
import {ApiRoutes} from "./apiRoutes";


const responseBody = (response: AxiosResponse) => response?.data;

export const httpActions = {
  get: (url: string, parameters:any={}) =>
    axios.get(url, {params: {...parameters}})
    .then(responseBody)
    .catch(err=> alert(err)),
  post: (url: string, body:any=null, parameters:any={}) =>
    axios.post(url, body, {params: {...parameters}})
    .then(responseBody)
}


export const callApi = {
  test: () => httpActions.get(ApiRoutes.API),
  getHistory: (username='') => httpActions.get(ApiRoutes.API, {username: username}),
}
