from django.contrib import admin
from django.urls import path
from .views  import APICars, APIDealer, APIComparing, OptionalDelete,APIOneDealer,APIOneComparing, APIGetOneCar

urlpatterns = [
    path('cars', APICars.as_view()),
    path('cars/<int:pk>', APICars.as_view()),
    path('dealers', APIDealer.as_view()),
    path('dealers/<int:pk>', APIDealer.as_view()),
    path('comparings', APIComparing.as_view()),
    path('comparings/<int:pk>', APIComparing.as_view()),
    path('optionaldeletecompares', OptionalDelete.as_view()),
    path('onecomparing/<int:pk>', APIOneComparing.as_view()),
    path('onedealer/<int:pk>', APIOneDealer.as_view()),
    path('onecar/<int:pk>', APIGetOneCar.as_view()),
]
