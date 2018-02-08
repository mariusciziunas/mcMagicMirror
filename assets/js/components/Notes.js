import React, {Component} from 'react';
import {Image, Container, Header} from 'semantic-ui-react';
import Note from './Note';

class Notes extends Component {

    render() {
        let notes;
        if (this.props.notes) {
            notes = this.props.notes.map(note => {

                return (
                    <div className='row'>
                        <Note note={note} />
                    </div>
                )
            });
        }
        return (
            <div className='ui container'>
                {notes}
            </div>
        )

    }

}

export default Notes;