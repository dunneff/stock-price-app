from django.db import models

# Create your models here.
class StockPortfolio(models.Model):
    """ A model representing a stock portfolio. """
    title = models.CharField(max_length=100)

class StockPortfolioItem(models.Model):
    """ A model representing stocks to be tracked in the portfolio. """
    portfolio_list = models.ForeignKey(
            'StockPortfolio',
            related_name='stocks', on_delete=models.CASCADE
            )
    title = models.CharField(max_length=100)
    # for now I'll follow the example of a description field.
    # later, this is where the data for a stock will go.
    # maybe I'll even be able to put in a graph
    description = models.TextField(blank=True, default='')
