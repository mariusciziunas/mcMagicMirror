import requests


class News:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = 'https://newsapi.org/'

    def get_news_by_source(self, source):
        news_api_response = requests.get(
            self.url + '/v1/articles?source=' + source + '&sortBy=top&apiKey=' + self.api_key)
        # print(self.url + '/v1/articles?source=' + source + '&sortBy=top&apiKey=' + self.api_key)
        news_result = []
        for api_item in news_api_response.json().get('articles'):
            result_item = {}
            result_item['title'] = api_item['title']
            result_item['description'] = api_item['description']
            result_item['urlToImage'] = api_item['urlToImage']
            news_result.append(result_item)
        return news_result
