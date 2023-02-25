from django.urls import path
from webapp.views.books import add_view, update_view, confirm_delete, delete_view
from webapp.views.base import index_view


urlpatterns = [
    path("", index_view, name='index'),
    path('book/', index_view),
    path('book/add/', add_view, name='book_add'),
    path('book/<int:pk>/update/', update_view, name='book_update'),
    path('book/<int:pk>/delete/', delete_view, name='book_delete'),
    path('book/<int:pk>/confirm_delete/', confirm_delete, name='confirm_delete'),
]