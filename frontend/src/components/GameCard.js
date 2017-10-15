import React, {Component} from 'react';

import './GameCard.css'

class GameCard extends Component {
    render() {
        return (
            <div className="game-card gradient">
                <figure>
                    <img src={this.props.img} alt={this.props.name}/>
                    <figcaption>
                        <div className="clash-card__unit-name">{this.props.name}</div>
                    </figcaption>
                </figure>

                <div className="clash-card__unit-stats clash-card__unit-stats--barbarian">
                    <div className="one-third">
                        <div className="stat">20<sup>S</sup></div>
                        <div className="stat-value">Training</div>
                    </div>

                    <div className="one-third">
                        <div className="stat">16</div>
                        <div className="stat-value">Speed</div>
                    </div>

                    <div className="one-third no-border">
                        <div className="stat">150</div>
                        <div className="stat-value">Cost</div>
                    </div>

                </div>
            </div>)
    }
}

export default GameCard;