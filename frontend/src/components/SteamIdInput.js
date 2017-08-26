import React, {Component} from 'react';
import {connect} from 'react-redux';

import {fetchWishlist} from '../actions/wishlistActions'
import './SteamIdInput.css';

class SteamIdInput extends Component {
    render() {
        return ( <div className="steam-id-input-container">
                <input autoFocus className="steam-id-input" type="text" placeholder="Enter your Steam ID..."
                       defaultValue="76561197974213560" ref="idInput"/>

                <button className="steam-id-input"
                        onClick={() => this.props.onHandleClick(this.refs.idInput.value)}>
                    Find my wishes!
                </button>
            </div>
        );
    }
}


const mapFetchWishlistToProps = dispatch => {
    return {
        onHandleClick:
            steamId => {
                dispatch(fetchWishlist(steamId));
            }
    }
};

export default connect(state => ({})
    , mapFetchWishlistToProps)(SteamIdInput);