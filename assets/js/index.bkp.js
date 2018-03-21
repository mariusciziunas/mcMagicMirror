import React from 'react';
import ReactDOM from 'react-dom';
import DashboardWrapper from './DashboardWrapper';
import YoutubeAlarm from './YoutubeAlarm';
import { BrowserRouter as Router, Route } from 'react-router-dom';

ReactDOM
    .render((
        <Router>
            <div className='style-template'>
                <Route exact path="/" component={DashboardWrapper} />
                <Route path="/alarm" component={YoutubeAlarm} />
            </div>
        </Router>
    ), document.getElementById('react-app')
);