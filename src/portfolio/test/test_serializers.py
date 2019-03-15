from django.test import TestCase
from portfolio import serializers

class StockPortfolioTestCase(TestCase):
    def test_portfolio_create(self):
        data = {
            'title': 'Test Portfolio',
            'stocks': [
                {
                    'title': 'Test stock 1',
                    'description': 'This is test stock 1'
                },
                {
                    'title': 'Test stock 2',
                    'description': 'This is test stock 2'
                }
            ]
        }

        serializer = serializers.StockPortfolio(data=data)
        self.assertTrue(serializer.is_valid())
        portfolio = serializer.save()
        self.assertEqual(portfolio.title, 'Test Portfolio')
        self.assertEqual(portfolio.stocks.count(), 2)

