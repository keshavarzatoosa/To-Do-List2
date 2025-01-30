from django_filters import rest_framework as filters
from todos.models import ToDoItem


class ToDoItemFilter(filters.FilterSet):

    class Meta:
        model = ToDoItem
        fields = {
            'title': ['exact', 'icontains'],
            'description': ['icontains'],
            'user': ['exact'],
        }