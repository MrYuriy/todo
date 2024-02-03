from django.urls import path
from todo.views import (
    TodoListView,
    TagListView,
    TodoCreateView,
    TodoDeleteView,
    TodoUpdateView,
    TagCreationView,
    TagUpdateView,
    TagDeleteView,
    TodoUpdateStatusView,
)

app_name = "todo"

urlpatterns = [
    path("", TodoListView.as_view(), name="todo-list"),
    path("todo/create/", TodoCreateView.as_view(), name="todo-create"),
    path("todo/<int:pk>/update/", TodoUpdateView.as_view(), name="todo-update"),
    path(
        "todo/<int:pk>/update/status/",
        TodoUpdateStatusView.as_view(),
        name="todo-status-update",
    ),
    path("todo/<int:pk>/delete/", TodoDeleteView.as_view(), name="todo-delete"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreationView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]
