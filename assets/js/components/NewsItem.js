import React, {Component} from 'react';
import { Image, Container, Header } from 'semantic-ui-react';

class NewsItem extends Component {

	render() {
		return (
			<Container as='div' className='two column row'>
				<Container as='div' className='three wide column no-padding-left-right'>
					<Image src={this.props.newsItem.urlToImage} />
				</Container>

				<Container as='div'  className='twelve wide column no-padding-left-right'>
					<Container as='div' className='row'>
						<Header as='h3'>{this.props.newsItem.title}</Header>
					</Container>

					<Container as='div' className='row'>
						{this.props.newsItem.description}
					</Container>
				</Container>

			</Container>
		)
	}

}

export default NewsItem