from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('api/users', views.create_user, name='users'),
#    path('api/users/<int:id>', views.user_by_id, name='users'),
#    path('api/auth', obtain_jwt_token, name='users'),
#    path('api/auth/login', views.login, name='users')
]