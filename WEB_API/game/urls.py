from django.urls import path


from . import views

urlpatterns = [
    path('<str:game_slug>/state/', views.state),

]
