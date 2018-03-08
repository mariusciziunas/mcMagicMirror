import React, {Component} from 'react';
import NewsItem from './NewsItem';
import { Button, Container, Header } from 'semantic-ui-react';

class News extends Component {

	render() {
		let newsItems
		if (this.props.news) {

			newsItems = this.props.news.map(item => {
				return (
					<NewsItem newsItem={item} />
				)
			});
		}
		return (
			<Container as='div'  className="ui grid">
				{newsItems}
			</Container>
		)
	}
}


export default News