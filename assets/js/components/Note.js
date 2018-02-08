import React, { Component } from 'react';

class Note extends Component {

    render() {
        let note;
        if (this.props.note) {
            note = this.props.note.text;
        }

        return(
            <div className='column'>
                {note}
            </div>
        )
    }

}

export default Note
