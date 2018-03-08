import React, {Component} from 'react';
import WeatherItem from './WeatherItem';

class Weather extends Component {

	render() {
		let forecast;
		if (this.props.forecast) {
		 	forecast = this.props.forecast.map(forecast => {
		 	return (
		 		<WeatherItem forecast={forecast} />
		 	)
		 });
		}
		return (
			<div className="ui grid">
				<div className="eight column row">
					{forecast}
				</div>
			</div>
		)
	}
}

export default Weather