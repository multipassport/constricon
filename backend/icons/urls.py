from django.urls import path
from icons import views

urlpatterns = [
    path(
        'icons/',
        views.IconListCreateView.as_view(),
        name='icon-list',
    ),
    path(
        'icons/<int:pk>/',
        views.IconRetrieveUpdateView.as_view(),
        name='icon-detail',
    ),
    path(
        'icons/<int:icon_pk>/parts/<int:pk>/',
        views.IconPartUpdateView.as_view(),
        name='part-detail',
    ),
]
