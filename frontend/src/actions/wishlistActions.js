import fetch from 'node-fetch'

export const FETCH_WISHLIST = 'FETCH_WISHLIST';

export function fetchWishlist(userSteamId) {
    return {
        type: FETCH_WISHLIST,
        payload: fetch('http://localhost:8000/wishlists/' + userSteamId).then((res) => res.json())
    }
}