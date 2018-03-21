import React, {Component} from 'react';

class WeatherItem extends Component {

	render() {
		
		return (
			<div className='column'>
				<div className='one column row'> 
					<div className='column'>
						{this.props.forecast.dt}
					</div>
					<div className='column'>
						{this.props.forecast.temp}
					</div>
					<div className='column'>
						{this.props.forecast.humidity}
					</div>
					<div className='column'>
						<img src={"static/images/" + this.props.forecast.icon + '.png'} />
						
					</div>
				</div>
			</div>
		)
	}
}

export default WeatherItem