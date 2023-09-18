from django.urls import path
from . import views

urlpatterns = [
    path('currencies/', views.CurrencyList.as_view()),
    path('exchange_rates/', views.ExchangeRateList.as_view()),
    path('conversions/', views.ConversionList.as_view()),
]