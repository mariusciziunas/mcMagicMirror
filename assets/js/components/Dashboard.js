import React, {Component} from 'react';
import {Button, Container, Header} from 'semantic-ui-react';
import Clock from 'react-live-clock';
import Weather from './Weather'
import News from './News';
import TrainDepartures from './TrainDepartures';
import BusArrivals from './BusArrivals';
import Calendar from './Calendar';
import Notes from './Notes';

class Dashboard extends Component {

    render() {
        return (
            // <Container as='div' className='ui grid container' style={margin: 0;}>
            <div className="ui grid container main-wrapper">

                <div className='three column relaxed row'>

                    <Container as='div' className='column'>
                        <Header as='h1'>
                            <Clock format={'D MMMM ddd (w) , YYYY HH:mm:ss'} ticking={true}/>
                        </Header>
                        <Weather forecast={this.props.weatherForecast}/>
                        <Header as='h2'>Don't forget</Header>
                        <Calendar calendar={this.props.calendar} />
                        <Header as='h2'>Notes</Header>
                        <Notes notes={this.props.notes} />
                    </Container>

                    <Container as='div' className='column'>
                        <TrainDepartures departures={this.props.trainDepartures}/>
                        <br />
                        <BusArrivals arrivals={this.props.busArrivals} />
                    </Container>

                    <Container as='div' className='column'>
                        <Container as='div'>
                            <Header as='h2'>World news</Header>
                            <Container as='div'>
                                <News news={this.props.worldNews}/>
                            </Container>

                            <Header as='h2'>Technology news</Header>
                            <Container as='div'>
                                <News news={this.props.techNews}/>
                            </Container>

                            <Header as='h2'>Sport news</Header>
                            <Container as='div'>
                                <News news={this.props.sportNews}/>
                            </Container>
                        </Container>
                    </Container>

                </div>
            </div>
        )
    }

}

export default Dashboard