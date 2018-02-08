import React, {Component} from 'react';
import $ from 'jquery';
import YouTube from 'react-youtube';
import { Redirect } from 'react-router-dom';

class YoutubeAlarm extends Component {

    state = { videoId: 'n_GFN3a0yj0s', isPlaying: false };

    constructor() {
        super();
        this.handleOnPlay = this.handleOnPlay.bind(this);
        this.handleOnEnd = this.handleOnEnd.bind(this);
        this.alarmStateToInactive = this.alarmStateToInactive.bind(this);
    }

    render() {
        if (this.state.finishedPlaying) {
            return (
                <Redirect to='/' />
            )
        }

        const opts = {
            height: '600',
            width: '800',
            playerVars: { // https://developers.google.com/youtube/player_parameters
                autoplay: 1,
                listType: 'playlist',
                list:'PL5SddC9I_hiFIFwngP44c6uEz6roo7BHW',
                modestbranding: 1
            }
        };
        return (
            <YouTube
                videoId={this.state.videoId}
                opts={opts}
                onReady={this.playerReady}
                onEnd={this.handleOnEnd}
                onPlay={this.handleOnPlay}
            />
        );
    }

    handleOnPlay(event) {
        this.setState({ isPlaying: true });
        event.target.setPlaybackQuality('highres');
    }

    handleOnEnd(event) {
        this.setState({ isPlaying: false });
        var promise = new Promise(function(resolve, reject) {
            setTimeout(function() {
                if (!this.state.isPlaying)  {
                    this.alarmStateToInactive();
                    this.setState({finishedPlaying: true});
                }
            }.bind(this), 5000);
        }.bind(this));
    }

    playerReady(event) {
        event.target.setVolume(100);
    }

    alarmStateToInactive() {
        $.ajax({
            url: '/disable-alarm',
            dataType: 'json',
            cache: false,
            success: function (data) {
                console.log('alarm disabled');
            }.bind(this),
                error: function (xhr, status, error) {
                console.log(error);
            }
        });
    }

}

export default YoutubeAlarm;