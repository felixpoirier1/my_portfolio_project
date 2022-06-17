from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('project-details/<str:pk>/', views.projectPage, name="projects"),
    #path('portfolio-opt/', views.portfolioOpt, name="portfolio-opt")
]