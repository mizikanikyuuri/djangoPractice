from django.urls import path

from . import views

app_name = 'practice1'
urlpatterns = [
    # ex: /practice1/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /practice1/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /practice1/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /practice1/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]