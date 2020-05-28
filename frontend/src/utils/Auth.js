import {Auth0Lock} from "auth0-lock";
import {getCookie, setCookie} from "./Cookies";

const URL = process.env.REACT_APP_AUTH0_URL;
const AUDIENCE = process.env.REACT_APP_AUTH0_API_AUDIENCE;
const CLIENT_ID = process.env.REACT_APP_CLIENT_ID;
const CALLBACK_URL = process.env.REACT_APP_CALLBACK_URL;
let RESPONSE_TYPE = 'token';

const OPTIONS = {
    rememberLastLogin: false,
    auth: {
        responseType: "token",
        redirect: true,
        autoParseHash: true,
        redirectUrl: CALLBACK_URL + 'hackathons',
        audience: AUDIENCE,
        params: {
            scope: "openid profile email",
        },
    },
};

const lock = new Auth0Lock(
    CLIENT_ID,
    URL + '.auth0.com',
    OPTIONS
);
/*
* Asynchronous actions in case of a /failed authentication
*/
lock.on("authenticated", (authResult) => {
    setCookie('accessToken', authResult.accessToken);
});
lock.on('authorization_error', (error) => console.log(error));
export default lock;



export function buildLoginLink(callbackInternalPath = '') {
    let link = 'https://';
    link += URL + '.auth0.com';
    link += '/authorize?';
    link += 'audience=' + AUDIENCE + '&';
    link += 'response_type=' + RESPONSE_TYPE + '&';
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

/*
* Check if a JWT token is present in cookies
* Return true/false
*/
export const getAccessTokenFromCookie = () => getCookie("accessToken");
export const isAuthenticated = () => !!getAccessTokenFromCookie();