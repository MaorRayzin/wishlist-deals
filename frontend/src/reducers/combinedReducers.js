import {combineReducers} from 'redux'

import wishlistReducer from './wishListReducer';

export default combineReducers({
    wishlist: wishlistReducer
})