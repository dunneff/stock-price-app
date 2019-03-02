from django.conf.urls import url
from django.contrib import admin

from stock_price_app/views/test import test_view

urlpatterns = [
        url(r'^$', test_view),
        url(r'^admin/', admin.site.urls),
        ]
