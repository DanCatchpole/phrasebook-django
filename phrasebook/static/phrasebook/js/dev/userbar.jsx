import React from 'react';
import {render} from 'react-dom';

class UserBar extends React.Component {

    render () {

        var createItem = function(item) {
            if (!item.active) {
                return <a href={item.url}>{item.title}</a>
            } else {
                return <a className="active" href={item.url}>{item.title}</a>
            }
        };

        return (
            <a className="user-bar">
                <img className="user-icon" src="https://dcatcher.me/assets/dcatcher.jpg" alt="userIcon"/>
                <img className="flag" src={"https://dcatcher.me/assets/" + this.props.details.current_language + ".svg"} alt=""/>
                <div className="progress-bar">
                    <span>Level {this.props.details.level}</span>
                    <div className="actual-progress"></div>
                </div>
            </a>
        );
    }
}

export default UserBar