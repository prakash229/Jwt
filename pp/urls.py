from django.urls import path
from .views import CreateUserAPIView,authenticate_user, UserRetrieveUpdateAPIView
 
urlpatterns = [
    path('create/', CreateUserAPIView.as_view()),
    path('obtain_token/', authenticate_user, name = 'authenticate_user'),
    path('update/', UserRetrieveUpdateAPIView.as_view()),
]