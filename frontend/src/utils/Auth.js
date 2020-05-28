import {getUrlParameter} from "./URL";

const URL = process.env.REACT_APP_AUTH0_URL;
const AUDIENCE = process.env.REACT_APP_AUTH0_API_AUDIENCE;
const CLIENT_ID = process.env.REACT_APP_CLIENT_ID;
const CALLBACK_URL = process.env.REACT_APP_CALLBACK_URL;

export function buildLoginLink(callbackInternalPath = '') {
    let link = 'https://';
    link += URL + '.auth0.com';
    link += '/authorize?';
    link += 'audience=' + AUDIENCE + '&';
    link += 'response_type=token&';
    link += 'client_id=' + CLIENT_ID + '&';
    link += 'redirect_uri=' + CALLBACK_URL + callbackInternalPath;
    return link;
}

export function buildLogoutLink() {
    let link = 'https://';
    link += URL + '.auth0.com';
    link += '/v2';
    link += '/logout?';
    link += 'returnTo=' + CALLBACK_URL + '&';
    link += 'client_id=' + CLIENT_ID;
    return link;
}

export const getAccessToken = () => getUrlParameter('access_token');
export const isAuthenticated = () => !!getAccessToken();