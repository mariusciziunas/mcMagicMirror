import React, {Component} from 'react';
import {Image, Container, Header} from 'semantic-ui-react';
import BusArrivalsItem from "./BusArrivalsItem";

class BusArrivals extends Component {

    render() {
        let arrivals;
        if (this.props.arrivals) {
            arrivals = this.props.arrivals.arrivals.map(arrival => {
                return (
                    <Container as='div'>
                        <Header as='h3'>
                            Bus {arrival.lineName} arrivals at {arrival.stationName} to {arrival.destinationName}
                        </Header>
                        <Container as='div' className='row'>
                            <BusArrivalsItem arrivals={arrival.expectedArrivals}/>
                        </Container>
                    </Container>
                )
            });
        }
        return (
            <Container as='div'>
                {arrivals}
            </Container>
        )

    }

}

export default BusArrivals