from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Todo
# Create your views here.

class TodosListView(TemplateView):
    template_name = "todo/todos.html"

    def get_context_data(self, **kwargs):
        context = super(TodosListView, self).get_context_data(**kwargs)
        context['todos'] = Todo.objects.all()
        return context

def get_todos(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        return render(request, 'todo/todo_list.html', {'todos': todos})


class TodosVueListView(TemplateView):
    template_name = "todo_vue.html"
