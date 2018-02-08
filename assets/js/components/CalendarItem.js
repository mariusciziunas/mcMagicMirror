import React, {Component} from 'react';
import {Image, Container, Header} from 'semantic-ui-react';


class CalendarItem extends Component {

    render() {
        let agenda;
        let styleClear = {
            clear: 'both'
        }
        if (this.props.events) {

            agenda = this.props.events.map(event => {
                return (
                <div class="ui grid no-margin-top">
                        <div className='left floated middle aligned content two wide column'>
                                {event.startDate} -{event.endDate}
                        </div>
                        <div className='left floated left aligned content twelve wide column'>
                                {event.title}
                        </div>

                </div>
                )
            });
        }
        return (
            <div >
                {agenda}
            </div>
        )

    }

}

export default CalendarItem;