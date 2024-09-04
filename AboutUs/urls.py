from django.urls import path
from . import views
app_name = 'AboutUs'
urlpatterns = [
    path('AboutUs/', views.AboutUs.as_view(), name='About_Us'),
]
