import React, {Component} from 'react';
import Dashboard from './components/Dashboard';
import $ from 'jquery';
import { Redirect } from 'react-router-dom';
import Notes from './components/Notes';

class DashboardWrapper extends Component {

    static apiServer = 'http://localhost:8000/';

    constructor() {
        super();
        this.state = {
            weatherForecast: []
        }
    }

    componentWillMount() {
        this.getWeatherForecast();
        this.getNews();
        this.getTrainDepartures();
        this.getBusArrivals();
        this.getCalendar();
        this.getNotes();
    }

    componentDidMount() {
        this.pollAlarmStatus();
        this.startPoll();
    }

    componentWillUnmount() {
        clearInterval(this.intervalNews);
        clearInterval(this.intervalWeather);
    }

    render() {
        if (this.state.isRedirectToAlarm) {
            return (
                <Redirect to='/alarm' />
            )
        }
        return (
            <div>
                <Dashboard weatherForecast={this.state.weatherForecast} worldNews={this.state.worldNews}
                           techNews={this.state.techNews} sportNews={this.state.sportNews} trainDepartures={this.state.trainDepartures} busArrivals={this.state.busArrivals}
                           calendar={this.state.calendar} notes={this.state.notes}/>

            </div>
        );
    }

    getNotes() {
        $.ajax({
            url: '/notes',
            dataType: 'json',
            cache: false,
            success: function (data) {
                this.setState({notes: data.notes});
            }.bind(this),
            error: function (xhr, status, error) {
                console.log(error);
            }
        });
    }

    getTrainDepartures() {
        $.ajax({
            // url: '/train-departures?stationCode=BFD&rowCount=10',
            url: '/train-departures',
            dataType: 'json',
            cache: false,
            success: function (data) {
                this.setState({trainDepartures: data});
            }.bind(this),
            error: function (xhr, status, error) {
                console.log(error);
            }
        });
    }

    getBusArrivals() {
        $.ajax({
            url: '/bus-arrivals',
            dataType: 'json',
            cache: false,
            success: function (data) {
                this.setState({busArrivals: data});
            }.bind(this),
            error: function (xhr, status, error) {
                console.log(error);
            }
        });
    }

    getWeatherForecast() {
        $.ajax({
            url: '/weather-forecast',
            dataType: 'json',
            cache: false,
            success: function (data) {
                this.setState({weatherForecast: data.forecast});
            }.bind(this),
            error: function (xhr, status, error) {
                console.log(error);
            }
        });
    }

    getCalendar() {
        $.ajax({
            url: '/calendar',
            dataType: 'json',
            cache: false,
            success: function (data) {
                this.setState({calendar: data.events});
            }.bind(this),
                error: function (xhr, status, error) {
                    console.log(error);
            }
        });
    }

    getNews() {
        this.__getNewsFromAPI('worldNews', 'world-news');
        this.__getNewsFromAPI('sportNews', 'sport-news');
        this.__getNewsFromAPI('techNews', 'technology-news');
    }

    __getNewsFromAPI(type, url) {
        $.ajax({
            url: url,
            dataType: 'json',
            cache: false,
            success: function (data) {
                this.setState({[type]: data.news});
            }.bind(this),
            error: function (xhr, status, error) {
                console.log(error);
            }
        });
    }

    pollAlarmStatus() {
        this.intervalNews = setInterval(function () {
            $.ajax({
                url: '/alarm-status',
                dataType: 'json',
                cache: false,
                success: function (data) {
                    if (data.status.value) {
                        this.enableLED();
                        this.setState({ isRedirectToAlarm: true });

                    }
                }.bind(this),
                error: function (xhr, status, error) {
                    console.log(error);
                }
            });
        }.bind(this), 1000);
    }

    enableLED() {
        $.ajax({
            url: '/turn-on-led',
            dataType: 'json',
            cache: false,
            success: function (data) {

            }.bind(this),
                error: function (xhr, status, error) {
                console.log(error);
            }
        });
    }

    startPoll() {
        this.intervalNews = setInterval(function () {
            this.getNews();
        }.bind(this), 600000);

        this.intervalWeather = setInterval(function () {
            this.getWeatherForecast();
        }.bind(this), 600000);

        this.intervalTrains = setInterval(function () {
            this.getTrainDepartures();
        }.bind(this), 60000);

        this.intervalBuses = setInterval(function () {
            this.getBusArrivals();
        }.bind(this), 60000);

        this.getCalendar = setInterval(function () {
            this.getCalendar();
        }.bind(this), 60000);

        this.intervalNotes = setInterval(function () {
            this.getNotes();
        }.bind(this), 60000);

    }

}

export default DashboardWrapper;