/*
 * Split the URL line and get parameters after.
 * Takes parameters after hash sign (#), not question mark (?).
 * For question mark (?) replace *.hash.* with *.search.*
 * TODO switch to storing the token in local storage or cookies.
 */
export function getUrlParameter(sParam) {
    let sPageURL = window.location.hash.substring(1),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;
    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return sParameterName[1] === undefined ? true : decodeURIComponent(sParameterName[1]);
        }
    }
}