from django.urls import path

from . import views

# this is set app name that is user in url mapping
# it is used in 'reverse(user:create)'
app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me')
]
