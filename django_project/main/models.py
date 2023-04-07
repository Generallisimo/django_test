from django.db import models

# создаем класс который подключи к бд 
class Task(models.Model):#где наследуем все от моделс она создаст таблицу для бд 
    # добавляем поля
    title =  models.CharField('Название', max_length=50)#для до 255 символов
    task = models.TextField('Описание')#для работы с большими текстами
    #  создаем фун с классом который отвечает за вывод объекта на экран
    def __str__(self) -> str:#где self будет обозначать объект
        return self.title