from django.contrib import admin
from .models import Task
# создаем таблицу чтобы её было видно
admin.site.register(Task)