from rest_framework import serializers
from portfolio import models

class StockPortfolioItem(serializers.ModelSerializer):
    class Meta:
        model = models.StockPortfolioItem
        fields = ('id', 'portfolio_list_id', 'title', 'description')

class StockPortfolio(serializers.ModelSerializer):
    stocks = StockPortfolioItem(many=True)

    class Meta:
        model = models.StockPortfolio
        fields = ('id', 'title', 'stocks')

    def create(self, validated_data):
        """
        Overide default create method
        This allows us to serialize whole portfolios with stocks
        validated_data is a dictionary of values for creating objects
        returns a portfolio object
        """
        stocks_data = validated_data.pop('stocks')
        portfolio = models.StockPortfolio.objects.create(**validated_data)
        for stock_data in stocks_data:
            stock_data['portfolio_list_id'] = portfolio.id
            models.StockPortfolioItem.objects.create(**stock_data)
        return portfolio
