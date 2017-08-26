import React, {Component} from 'react';

import './GameCard.css'

class GameCard extends Component {
    render() {
        return <div className="game-card">
                <figure>
                    <img src={this.props.img} alt={this.props.name}/>
                    <figcaption>
                        {this.props.name}
                    </figcaption>
                </figure>
        </div>
    }
}

export default GameCard;