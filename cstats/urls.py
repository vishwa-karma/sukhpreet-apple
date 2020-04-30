from django.urls import path
from . import views

app_name = 'cstats'

urlpatterns = [
    path('/accounts/login/', views.cluster_list, name='cluster_list'),
    path('cluster/<int:pk>/edit/', views.cluster_edit, name='cluster_edit'),

]