from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from backend.views import FilmViewSet, UserViewSet, api_root
from rest_framework import renderers

film_list = FilmViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

film_detail = FilmViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('films/', film_list, name='film-list'),
    path('films/<int:pk>/', film_detail, name='film-detail'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail')
])