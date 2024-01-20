from django.urls import path
from api import views
urlpatterns = [
    path('currencyexchange/', views.CurrencyExchange.as_view()),
    # path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]