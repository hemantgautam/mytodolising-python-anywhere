from django import forms
from .models import TodoList, BoardList


class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ["userid", "item", "completed", "board_id"]


class BoardListForm(forms.ModelForm):
    class Meta:
        model = BoardList
        fields = ["board_name", "userid"]
