import {getPendingType, getFulfilledType, getRejectedType} from '../actions/actions';
import {FETCH_WISHLIST} from '../actions/wishlistActions';

function createWishlistState(prevState, nextState = {}) {
    if (nextState.wishlist === undefined) {
        nextState.wishlist = [];
    }
    if (nextState.isFetching === undefined) {
        nextState.isFetching = false;
    }
    if (nextState.error === undefined) {
        nextState.error = null;
    }
    return {...prevState, ...nextState};
}

export default function reducer(state, action) {
    switch (action.type) {
        case getPendingType(FETCH_WISHLIST): {
            return createWishlistState(state, {isFetching: true});
        }
        case getFulfilledType(FETCH_WISHLIST): {
            console.log(action.payload);
            return createWishlistState(state, {wishlist: action.payload});
        }
        case getRejectedType(FETCH_WISHLIST): {
            return createWishlistState(state, {error: action.payload.name});
        }
        default:
            return createWishlistState(state);
    }
}