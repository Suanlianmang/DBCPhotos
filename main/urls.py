from django.urls import path
from . import views
from .views import UploadView

urlpatterns = [
    path('', views.home, name='dbc-home'),
    path('upload/', UploadView.as_view(), name='upload'),
    path('<str:name>/', views.catagory, name='catagory'),
]