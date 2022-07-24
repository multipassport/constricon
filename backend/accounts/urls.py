from accounts import views
from django.urls import path

urlpatterns = [
    path(
        'users/<int:pk>/',
        views.UserUpdateView.as_view(),
        name='user-detail',
    ),
]
