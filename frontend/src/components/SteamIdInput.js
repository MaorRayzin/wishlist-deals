import React, {Component} from 'react';
import {connect} from 'react-redux';

import {fetchWishlist} from '../actions/wishlistActions'
import './SteamIdInput.css';

class SteamIdInput extends Component {

    constructor() {
        super();
        this.state = {
            value: ''
        }
    }

    render() {
        return ( <div id="steam-id-input-container">
                <input className="steam-id-input" type="text" placeholder="Enter your Steam ID..." ref="idInput"/>
                <input className="steam-id-input" type="button" value="Find my wishes!"
                       onClick={() => this.props.onHandleClick(this.refs.idInput.value)}/>
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

export default connect(state => {return {
}}, mapFetchWishlistToProps)(SteamIdInput);