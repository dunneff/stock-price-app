from django.test import TestCase
from portfolio.models import StockPortfolio, StockPortfolioItem

class StockPortfolioTestCase(TestCase):
    def test_portfolio(self):
        StockPortfolio.objects.create(title='Test Portfolio')
        portfolio = StockPortfolio.objects.get(title='Test Portfolio')
        self.assertEqual(portfolio.title, 'Test Portfolio')
        portfolio.delete()
        try:
            retrieved_portfolio = StockPortfolio.objects.get(title='Test Portfolio')
        except StockPortfolio.DoesNotExist:
            retrieved_portfolio = None
        self.assertEqual(retrieved_portfolio, None)

    def test_portfolio_stock(self):
        portfolio = StockPortfolio.objects.create(title='Test Portfolio')
        portfolio_stock = StockPortfolioItem.objects.create(
                portfolio_list=portfolio,
                title='Test Stock',
                description="This is a test stock item in the portfolio"
                )
        self.assertEqual(portfolio.stocks.count(), 1)
        self.assertEqual(portfolio.stocks.first(), portfolio_stock)
        portfolio.delete()
        try:
            retrieved_item = StockPortfolioItem.objects.get(title='Test Stock')
        except StockPortfolioItem.DoesNotExist:
            retrieved_item = None
        self.assertEqual(retrieved_item, None)
