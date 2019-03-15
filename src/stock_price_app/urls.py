from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from portfolio import views

urlpatterns = [
        url(r'^portfolio$', views.StockPortfolio.as_view()),
        url(r'^portfolio/(?P<portfolio_list_id>[0-9]+)$', views.StockPortfolio.as_view()),
        url(r'^portfolio/(?P<portfolio_list_id>[0-9]+)/stocks$', views.StockPortfolioItem.as_view()),
        url(r'^portfolio/stocks/(?P<stock_id>[0-9]+)$', views.StockPortfolioItem.as_view()),
        ]

urlpatterns = format_suffix_patterns(urlpatterns)
