from django.urls import path

from .views import TodosListView, get_todos

urlpatterns = [
    path('', TodosListView.as_view(), name='todo'),
    path('get-todos/', get_todos, name='get_todos'),
]
