from .models import Task
# импорт для работы с формами
from django.forms import ModelForm, TextInput, Textarea

# создаем класс в честь работы с моделью
class TaskForm(ModelForm):
    # укз класс который отвечает за настройки
    class Meta:
        # укз с чем будем работать
        model = Task
        # укз какие поля будут в форме
        fields = ["title", "task"]#они будут совпадать с навазниями в бд
        # создаем виджет для стилизации полей
        widgets = {
            'title':TextInput(
                #прописываем атрибуты стилей
                attrs={
                    'class': 'form-control',
                    'placeholder':'Введите название'    
                }),
            'task':Textarea(
                #прописываем атрибуты стилей
                attrs={
                    'class': 'form-control',
                    'placeholder':'Введите описание'    
                })
            }