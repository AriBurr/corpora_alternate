from django.urls import path
from . import views

urlpatterns = [
    path('substrings/', views.RecommenderView.as_view(), name='recommender_view'),
]