from django.contrib import admin
from .models import ToDoItem
from .models import Objectives 
# Register your models here.
admin.site.register(ToDoItem)
admin.site.register(Objectives)
