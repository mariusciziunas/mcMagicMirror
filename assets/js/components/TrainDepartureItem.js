import React, {Component} from 'react';
import {Button, Container, Header} from 'semantic-ui-react';

class TrainDepartureItem extends Component {

    render() {
        let departures;
        if (this.props.departure) {
            departures = this.props.departure.map(departure => {
                return (
                    <Container as='div' className='center aligned column '>
                        {departure.std}
                                <Container as='span' className='highlight'>
                                    {departure.etd}
                                </Container>
                                pl. {departure.platform}
                    </Container>
                )
            });
        }
        return (
            <Container as='div' className='ui celled grid six column wide'>
                {departures}
            </Container>
        )
    }
}

export default TrainDepartureItem