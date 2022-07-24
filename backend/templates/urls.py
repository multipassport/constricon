from django.urls import path
from templates import views

urlpatterns = [
    path(
        'templates/',
        views.TemplateListView.as_view(),
        name='template-list',
    ),
    path(
        'templates/<int:pk>/',
        views.TemplateRetrieveView.as_view(),
        name='template-detail',
    ),
    path(
        'packs/',
        views.PackListView.as_view(),
        name='pack-list',
    ),
    path(
        'items/',
        views.ItemListView.as_view(),
        name='item-list',
    ),
    path(
        'items/<int:pk>/',
        views.ItemRetrieveView.as_view(),
        name='item-detail',
    ),
]
