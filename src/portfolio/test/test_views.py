import json
from django.test import TestCase, Client
from portfolio import models

class StockPortfolioTestCase(TestCase):
    """
    testing the stock portfolio views
    """

    def setUp(self):
        self.client = Client()
        self.test_portfolio = models.StockPortfolio.objects.create(title='Test portfolio of stocks')
        super(StockPortfolioTestCase, self).setUp()

    def test_portfolio_stock_post_delete(self):
        """
        check that adding and removing stocks to and from a portfolio works
        """
        post_data = {
                'title': 'Test stock',
                'desctiption': "Whadya know, it's a test!"
                }
        response = self.client.post(
                '/portfolio/{0}/stocks'.format(self.test_portfolio.id),
                json.dumps(post_data),
                content_type='application/json')

        self.assertEqual(response.status_code, 200)

        stock_id = response.data['id']
        response = seft.client.delete('/portfolio/stocks/{0}'.format(stock_id))

        self.assertEqual(response.status_code, 204)

    def test_portfolio_get_post_delete(self):
        """
        check that we can create, retrieve, and destroy whole portfolios
        """
        post_data = {
                'title': 'Test portfolio',
                'stocks': [
                    {
                        'title': 'Test stock 1',
                        'description': 'A test stock, number 1'
                        },
                    {
                        'title': 'Test stock 2',
                        'description': 'A test stock, number 2'
                        }
                    ]
                }
        response = self.client.post('/portfolio',
                json.dumps(post_data),
                content_type='application/json')
        self.assertEqual(response.status_code, 200)
        portfolio_list_id = response.data['id']
        received_portfolios = dict(response.data)
        print("response.content")
        print(response.content)
        print("end response.content")

        is_present = False
        found_portfolio = None
        print(received_portfolios)
        for received_portfolio in received_portfolios:
            print(received_portfolio)
            if received_portfolio['id'] == portfolio_list_id:
                is_present = True
                found_portfolio = received_portfolio
                break

        self.assertTrue(is_present)
        self.assertEqual(found_portfolio['title'], post_data['title'])
        self.assertEqual(len(found_portfolio['stocks']), len(post_data['stocks']))

        for i in range(0, len(found_portfolio['items'])):
            found = found_portfolio['items'][i]
            expected = post_data['items'][i]
            self.assertEqual(found['title'], expected['title'])
            self.assertEqual(found['description'], expected['description'])

        response = self.client.delete('/portfolio/{0}'.format(portfolio_list_id))
        self.assertEqual(response.status_code, 204)
