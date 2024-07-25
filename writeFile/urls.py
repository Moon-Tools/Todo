from django.urls import path
from .views import TaskListCreateView, TaskRetriveUpdateDestroyView

urlpatterns = [
  path("task/", TaskListCreateView.as_view(), name="Task-List-Create"),
  path("task/<int:pk>", TaskRetriveUpdateDestroyView.as_view(), name="Task-Retrive-Update-Delete")
]