from django.urls import path
from . import views

urlpatterns = [
    path('api/dogs', views.DogList.as_view(), name='dog_list'), # api/dog will be routed to the ContactList view for handling
    path('api/dogs/<int:pk>', views.DogDetail.as_view(), name='dog_detail'), # api/dog will be routed to the DogDetail view for handling
]
