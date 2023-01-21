from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>', views.project_detail, name='project_detail'),
    path('<int:pk>/add_comment/', views.add_comment, name='add_comment'),
]
