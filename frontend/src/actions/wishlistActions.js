import 'whatwg-fetch'

export const FETCH_WISHLIST = 'FETCH_WISHLIST';
export const FETCH_GAME_DETAILS = 'FETCH_GAME_DETAILS';

export function fetchWishlist(userSteamId) {
    return {
        type: FETCH_WISHLIST,
        payload: fetch('http://localhost:8000/wishlists/' + userSteamId).then((res) => res.json())
    }
}

export function fetchGameDetails(steamAppId) {
    return {
        type: FETCH_GAME_DETAILS,
        payload: fetch('http://localhost:8000/details/' + steamAppId).then((res) => res.json())
    }
}