import {PENDING, FULFILLED, REJECTED} from 'redux-promise-middleware';
import {FETCH_WISHLIST} from '../actions/wishlistActions';

export default function reducer(state = {}, action) {
    switch (action.type) {
        case FETCH_WISHLIST + '_' + FULFILLED: {
            return {...state, wishlist:action.payload.wishlist};
        }
    }
    return {...state};
}