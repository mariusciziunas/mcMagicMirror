import React, {Component} from 'react';
import {Button, Container, Header} from 'semantic-ui-react';

class BusArrivalsItem extends Component {

    render() {
        let arrivals;

        if (this.props.arrivals) {

            arrivals = this.props.arrivals.map(arrival => {
                return (
                    <Container as='div' className='column'>
                        {arrival}
                    </Container>
                )
            });
        }
        return (
            <Container as='div' className='ui celled grid six column wide'>
                {arrivals}
            </Container>
        )
    }
}

export default BusArrivalsItem