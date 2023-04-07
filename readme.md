Для этого выполните следующую команду в терминале:
python3 -m venv myenv

Активируйте виртуальное окружение:
source myenv/bin/activate

Установка Django:
pip install django

Создайте Django проект:
django-admin startproject django_project

Запустите Django проект:
cd myproject
python manage.py runserver

создаем приложение внутри проекта для фун-ла сайта:
python3 manage.py startapp main 
Файлы:
init - инцилизатор
admin - для отображения моделей в админке
apps - укз название файла и также можно указывать конкретные настройки 
models - таблицы которые будут добавлясть в бд 
tests - для тестировки
views - для вывода всех старниц
urls - туда будем добавлять обрабокту основного url
temlates/main - здесь все шаблоны где название приложение папки
forms - здесь обработка форм для страницы 

Создание миграции:
python3 manage.py makemigrations - для создание модели
python3 manage.py migrate - мигрируем

Создаем админа:
python3 manage.py createsuperuser

