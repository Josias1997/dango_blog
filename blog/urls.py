from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('article/<int:id_article>', views.view_article),
    path('article/<str:tag>', views.list_articles_by_tag),
    path('article/<int:year>/<int:mont>', views.list_articles),
    path('redirection', views.view_redirection),
    path('date', views.actual_date),
    path('addition/<int:number1>/<int:number2>', views.addition),
]
