import React, {Component} from 'react';
import {connect} from 'react-redux';

import './WishlistView.css';
import {fetchGameDeals} from '../actions/wishlistActions'
import GameCard from './GameCard';

class WishlistView extends Component {
    getGameCards() {
        let cards = this.props.wishlist.map(game => {
            return <GameCard key={game.id} className="game-card" name={game.name} img={game.img}/>
        });
        return <div className="game-cards">
            {cards}
        </div>
    }

    getViewContent() {
        if (this.props.isFetching) {
            return <div className="wishlist-loader"/>
        }
        if (this.props.error !== null) {
            return <h1 className="wishlist-error">Error occurred: {this.props.error}</h1>
        }
        return this.getGameCards();
    }

    render() {
        return <div className="wishlist-view">
            {this.getViewContent()}
        </div>
    }
}

const mapFetchGameDealsToProps = dispatch => {
    return {
        fetchGameDeals:
            steamAppId => {
                dispatch(fetchGameDeals(steamAppId));
            }
    }
};

const mapStateToProps = (state) => {
    return {
        wishlist: state.wishlist.wishlist,
        isFetching: state.wishlist.isFetching,
        error: state.wishlist.error
    }
};

export default connect(mapStateToProps, mapFetchGameDealsToProps)(WishlistView);

