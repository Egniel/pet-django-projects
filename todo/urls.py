from django.urls import path

from .views import TodosListView, get_todos, TodosVueListView

urlpatterns = [
    path('', TodosListView.as_view(), name='todo'),
    path('get-todos/', get_todos, name='get_todos'),
    path('vue', TodosVueListView.as_view(), name='todo_vue'),
]
