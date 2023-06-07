from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.wiki, name="wiki"),
    path("search/", views.search, name="search"),
    path("new_page/", views.create_new_page, name="create_new_page"),
    path("edit_page/<str:current_title>", views.edit_page, name="edit_page"),
    path("random_page/", views.random_page, name="random_page")
]
