from django.shortcuts import render, redirect
# импорт библиотки для запроса
# from django.http import HttpResponse
# импорт для вывода бд на стр 
from .models import Task
# импорт формы
from .forms import TaskForm

# создаем фун для сайта чтобы он что-т показывал или обрабатывал
def index(request):
    # для вывода простой строки
    # return HttpResponse("<h4>Hello Word</h4>")
    
    # вывод из бд ищем все
    tasks = Task.objects.all()
    # для вывода шаблона 
    return render(request, 'main/index.html', {'title': 'Главная страница', 'tasks': tasks})#вначале передаем заданный параметр потом выводим страницу и передаем ключи для вывода title и из бд в шаблон
# вывод второй страницы
def about(request):
    return render(request, 'main/about.html')
# создание такса через страницу
def create(request):
    error = ''
    # для отправки сообщений то мы используем метод post делаем фун
    if request.method == 'POST':
        # задаем получение данных
        form = TaskForm(request.POST)
        # проверяем валидность
        if form.is_valid():
            # сохраняем
            form.save()
            # редирект
            return redirect('home')
        else:
            error = "Неправильно"
    # переменная для формы
    form = TaskForm()
    # создадим переменную которая будет хранить в себе ключи
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'main/create.html', context)