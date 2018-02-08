import React, {Component} from 'react';
import { Button, Container, Header } from 'semantic-ui-react';
import TrainDepartureItem from './TrainDepartureItem';

class TrainDepartures extends Component {


    render() {
        let departures;
        if (this.props.departures) {
            departures = this.props.departures.destinations.map(departure => {
                return (
                    <Container as='div'>
                        <Header as='h3'>Trains from {this.props.departures.location} to {departure.name}</Header>
                        <TrainDepartureItem departure={departure.departures}/>
                    </Container>
                )
            });
        }
        return (
            <Container as='div'>
                {departures}
            </Container>
        )
    }



}

export default TrainDepartures