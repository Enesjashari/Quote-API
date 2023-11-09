from django.urls import path
from . import views

urlpatterns = [
    path('all-quotes', views.QuoteList.as_view(), name='quote-list'),
    path('quote/<int:pk>/', views.QuoteDetail.as_view(), name='quote-detail'),
    path('quotes/', views.get_quotes, name='get-quotes'),
    path('random', views.random_quote_json, name='random'),
    path('contribute', views.contribute, name='contribute'),
    path('', views.index, name='index'),

]
