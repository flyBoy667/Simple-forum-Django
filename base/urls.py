from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),

    path("", views.home, name="home"),
    path("room/<str:pk>/", views.room_detail, name="room-detail"),
    path("create-room/", views.create_room, name="room-create"),
    path("update/<str:pk>/", views.update_room, name="update-room"),
    path("delete/<str:pk>/", views.delete_room, name="delete-room"),
]
