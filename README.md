# Название проекта
api_yatube

# Описание проекта
API имитирующая социальную сеть с возможностью создавать, просматривать, редактировать посты на различную тематику. А также с возможностью комментирования постов и подписок на авторов.

# Технологии
Для создания проекта использовались следующие технологии:
    Язык программирования Python 3.9;
    Библиотеки: django_rest_framework, djoser, django_filter;

# Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

git clone https://github.com/FILL9214/api_final_yatube.git
cd api_final_yatube
Cоздать и активировать виртуальное окружение:

python3 -m venv env
source env/bin/activate
Установить зависимости из файла requirements.txt:

python3 -m pip install --upgrade pip
pip install -r requirements.txt
Выполнить миграции:

python3 manage.py migrate
Запустить проект:

python3 manage.py runserver

# Примеры использования
Запрос аторизованного пользователя ко всем постам:
![Screenshot](https://github.com/FILL9214/api_final_yatube/blob/master/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-04-29%20%D0%B2%2015.12.25.png)
Запрос неавторизованного пользователя ко всем группам:
![Screenshot](https://github.com/FILL9214/api_final_yatube/blob/master/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-04-29%20%D0%B2%2015.13.03.png)

# Автор
Филипп Истомин
