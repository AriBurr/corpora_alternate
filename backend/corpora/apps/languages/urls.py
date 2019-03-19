from django.urls import path
from . import views

urlpatterns = [
    path('languages/', views.LanguageViewSet.as_view(), name='language_list'),
]