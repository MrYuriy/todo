from django.shortcuts import render
from .models import Tag, Todo
from django.views import generic, View
from django.urls import reverse, reverse_lazy
from .forms import TodoCreationForm, TagCreationForm
from django.shortcuts import get_object_or_404, redirect


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo/tag_list.html"
    paginate_by = 5


class TagCreationView(generic.CreateView):
    model = Tag
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo:tag-list")
    form_class = TagCreationForm


class TagUpdateView(generic.UpdateView):
    model = Tag
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo:tag-list")
    form_class = TagCreationForm


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todo/tag_confirm_delete.html"
    success_url = reverse_lazy("todo:tag-list")


class TodoListView(generic.ListView):
    model = Todo
    template_name = "todo/index.html"
    paginate_by = 5


class TodoCreateView(generic.CreateView):
    model = Todo
    template_name = "todo/todo_form.html"
    success_url = reverse_lazy("todo:todo-list")
    form_class = TodoCreationForm


class TodoDeleteView(generic.DeleteView):
    model = Todo
    template_name = "todo/todo_confirm_delete.html"
    success_url = reverse_lazy("todo:todo-list")


class TodoUpdateView(generic.UpdateView):
    model = Todo
    template_name = "todo/todo_form.html"
    success_url = reverse_lazy("todo:todo-list")
    form_class = TodoCreationForm


class TodoUpdateStatusView(View):
    def post(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        todo.completed = request.POST.get("status", not todo.completed)
        print(todo.completed)
        todo.save()
        return redirect("todo:todo-list")
