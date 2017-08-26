import React, {Component} from 'react';
import logo from '../steam_logo.svg';
import SteamIdInput from './SteamIdInput';
import WishlistView from './WishlistView';

import './App.css';


class App extends Component {
    render() {
        return (
            <div className="App">
                <div className="App-header">
                    <img src={logo} className="App-logo" alt="logo"/>
                    <h2>Welcome to Steam Wishlist Deals</h2>
                </div>
                <div className="App-intro">
                    <SteamIdInput/>
                    <WishlistView/>
                </div>
            </div>
        );
    }
}

export default App;
