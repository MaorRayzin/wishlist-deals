import React, {Component} from 'react';

import './GameCard.css'

class GameCard extends Component {
    render() {
        return <article className="game-card"><h5>{this.props.name}</h5></article>
    }
}

export default GameCard;