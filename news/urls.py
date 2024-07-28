from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_new_info, name="add_new_info"),
    path("<int:news_id>/", views.detail, name="detail"),
    path("<int:news_id>/comment/", views.add_comment, name="add_comment"),

]