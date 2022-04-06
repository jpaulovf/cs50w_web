from django.urls import path
from . import views 

urlpatterns = [
    # Choosing what to show when the empty "" url is visited
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("joao", views.joao, name="joao")
]