import 'whatwg-fetch'

export const FETCH_WISHLIST = 'FETCH_WISHLIST';
export const FETCH_GAME_DETAILS = 'FETCH_GAME_DETAILS';
export const FETCH_HLTB_DETAILS = 'FETCH_HLTB_DETAILS';

export function fetchWishlist(userSteamId) {
    return {
        type: FETCH_WISHLIST,
        payload: fetch('http://localhost:8000/wishlists/' + userSteamId).then((res) => res.json())
    }
}

export function fetchHltbDetails(gameSteamId) {
    return {
        type: FETCH_HLTB_DETAILS,
        payload: fetch('http://localhost:8000/hltb/' + gameSteamId).then((res) => res.json())
    }
}

export function fetchGamesDeals(steamAppId) {
    return {
        type: FETCH_GAME_DETAILS,
        steamAppId,
        payload: fetch('http://localhost:8000/deals/' + steamAppId).then((res) => res.json())
    }
}
