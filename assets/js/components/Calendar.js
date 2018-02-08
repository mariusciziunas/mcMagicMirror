import React, {Component} from 'react';
import {Image, Container, Header} from 'semantic-ui-react';
import CalendarItem from './CalendarItem';

class Calendar extends Component {

    render() {
        let calendar;
        if (this.props.calendar) {
            calendar = this.props.calendar.map(agenda => {

                return (
                    <div>
                        <h3 class='no-margin'>{agenda.day}</h3>
                        <CalendarItem events={agenda.events} />
                    </div>
                )
            });
        }
        return (
            <div >
                {calendar}
            </div>
        )

    }

}

export default Calendar;