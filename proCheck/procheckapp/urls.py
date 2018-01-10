from django.conf.urls import url
from procheckapp import views

app_name = 'procheckapp'

urlpatterns = [

    url(r'^register/', views.register, name='register'),
    url(r'^userlogin/', views.user_login, name='user_login'),
    url(r'^userlogin/', views.user_logout, name='user_logout'),

]
