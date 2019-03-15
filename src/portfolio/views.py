from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from portfolio import serializers, models

class StockPortfolio(APIView):
    """
    Lists all portfolios when the GET method is called
    Add a new portfolio when POST method is called
    Delete a portfolio when the DELETE method ic called
    """

    def get(self, request, format=None):
        """
        this is how to get portfolios from the database
        """
        portfolios = models.StockPortfolio.objects.all()

        serializer = serializers.StockPortfolio(portfolios, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        """
        make a new portfolio based on the request
        """
        serializer = serializers.StockPortfolio(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, portfolio_list_id, format=None):
        try:
            portfolio_list = models.StockPortfolio.objects.get(id=portfolio_list_id)
            portfolio_list.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except models.StockPortfolio.DoesNotExist:
            raise Http404

class StockPortfolioItem(APIView):
    """
    Adding and removing stocks from the portfolios
    """
    def post(self, request, portfolio_list_id, format=None):
        try:
            portfolio = models.StockPortfolioItem.objects.get(id=portfolio_list_id)
            serializer = serializers.StockPortfolioItem(data=request.data)

            if serializer.is_valid():
                serializer.validated_data['portfolio_list_id'] = portfolio_list_id
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except models.StockPortfolio.DoesNotExist:
            raise Http404

    def delete(self, request, stock_id, format=None):
        try:
            stock = models.StockPortfolioItem.objects.get(id=stock_id)
            stock.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except models.StockPortfolioItem.DoesNotExist:
            return Http404
