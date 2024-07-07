from django.urls import path

from . import views

urlpatterns = [
    path("", view=views.index, name="index"),
    path("<int:first>/add/<int:second>/", view=views.add, name="add"),
    path("transform/<str:text>/", view=views.upper, name="upper"),
    path("check/<str:word>/", view=views.palindrome, name="palindrome"),
    path("calc/<int:first>/<str:operation>/<int:second>/", view=views.calculate, name="calculate")
]