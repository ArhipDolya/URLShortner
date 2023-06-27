from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('save_in_db', views.save_in_db, name='save_in_db'),
    path('<str:link>', views.generate_webpage_link, name='generate_webpage_link')
]