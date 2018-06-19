import React from 'react';
import {render} from 'react-dom';
import UserBar from "./userbar.jsx"

class Header extends React.Component {

    render () {

        var createItem = function(item) {
            if (!item.active) {
                return <a href={item.url}>{item.title}</a>
            } else {
                return <a className="active" href={item.url}>{item.title}</a>
            }
        };

        return (
            <header>
                <div className="contents">
                    <div className="logo">
                        <a href={this.props.homeLink}><img src="https://dcatcher.me/assets/pb-text-horiz-color.svg" alt=""/></a>
                    </div>
                    <div className="navigation">
                        {this.props.items.map(createItem)}
                    </div>
                    <div className="sticky-push"></div>
                    <UserBar details={this.props.details}/>
                </div>
            </header>
        );
    }
}

export default Header