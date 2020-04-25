from django.contrib import admin
from .models import TodoList, BoardList


# Register your models here.
# admin.site.register(TodoList)
# admin.site.register(BoardList)

class ListEntryAdmin(admin.ModelAdmin):
    list_display = ('item', 'userid', 'board_id')
    # search_fields = ['title']

    # def __init__(self):
    #     return self.user.username


class BoardEntryAdmin(admin.ModelAdmin):
    list_display = ('board_name', 'userid')
    # list_filter = ['board_name', 'userid']
    search_fields = ['board_name', 'userid']


admin.site.register(TodoList, ListEntryAdmin)
admin.site.register(BoardList, BoardEntryAdmin)
