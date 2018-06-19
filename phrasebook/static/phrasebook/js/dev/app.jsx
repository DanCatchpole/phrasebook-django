import React from 'react';
import {render} from 'react-dom';
import Header from './header.jsx'

class App extends React.Component {
    render () {
        return (
            <div>
                <Header homeLink={homeLink} items={menuItems} details={this.props.details}/>
                <main> <p>Hello World</p> </main>
            </div>
        );
    }
}

render(<App details={userDetails}/>, document.getElementById('app'));
