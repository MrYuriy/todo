from django.shortcuts import render
from .models import Tag, Todo
from django.views import generic
from django.urls import reverse, reverse_lazy


# Create your views here.

class TagListView(generic.ListView):
    model = Tag
    template_name = "todo/tag_lis.html"
    content_object_name = "tag_list"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")
    template_name = "todo/tag_form.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")
    template_name = "todo/tag_form.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")
    template_name = "todo/tag_form.html"


class TodoListView(generic.ListView):
    model = Todo
    template_name = "todo/todo_list.html"
    content_object_name = "todo_list"


class TodoCreateView(generic.CreateView):
    model = Todo
    fields = "__all__"
    template_name = "todo/todo_list.html"
    success_url = reverse_lazy("todo:todo-list")


class TodoUpdateView(generic.UpdateView):
    model = Todo
    fields = "__all__"
    template_name = "todo/todo_list.html"
    success_url = reverse_lazy("todo:todo-list")


class TodoDeleteView(generic.DeleteView):
    model = Todo
    field = "__all__"
    template_name = "todo/todo_list.html"
    success_url = reverse_lazy("todo:todo-list")
    