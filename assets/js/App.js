import React, {Component} from 'react';
import { StaticRouter, Switch, Route } from 'react-router';
import DashboardWrapper from './DashboardWrapper';
import YoutubeAlarm from './YoutubeAlarm';


class App extends Component {

    render() {


        return (
            <div>
                <Switch>
                    <Route path="/" component={DashboardWrapper} />
                    <Route path="/alarm" component={YoutubeAlarm} />
                </Switch>
            </div>
        )
    }
}

export default App
