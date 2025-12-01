from newsdataapi import NewsDataApiClient
from django.conf import settings

class NewsAPIService:
    def __init__(self):
        self.api = NewsDataApiClient(apikey=settings.NEWS_API_KEY)

    def get_latest_news(self, category='technology', country='in', limit=10):
        response = self.api.latest_api(
            q=category,
            country=country,
            language='en',
        )
        articles = []
        for item in response.get('results', []):
            articles.append({
                'title': item.get('title', 'No title'),
                'description': item.get('description', ''),
                'pubDate': item.get('pubDate'),
                'image_url': item.get('image', ''),
                'link': item.get('link', ''),
                'source_id': item.get('source_id', 'Unknown'),
            })
        return articles
