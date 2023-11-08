from django.urls import path
from . import views

urlpatterns = [
    path('quotes/', views.QuoteList.as_view(), name='quote-list'),
    path('quotes/<int:pk>/', views.QuoteDetail.as_view(), name='quote-detail'),
    path('quotess/', views.get_quotes, name='get-quotes'),
    path('random', views.random_quote_json, name='random'),

]
