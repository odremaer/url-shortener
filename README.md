## Для запуска проекта понадобится Python>= 3.4.
## Далее:

### Если вы используете Pycharm:
- Откройте проект в Pycharm'e.
- Создайте новую виртуальную среду (для этого нужно перейти в Settings > Project: url-shortener > Project Interpreter
  далее справа от выбора интерпретатора нажмите на конпку настроек > Add и создайте New enviroment, поставив в Base interpreter
  ваш путь до вашего питона)
- Перейдите в терминал PyCharm'a (слева от пути к проекту должна быть надпись (venv), если таковой нет нажмите + над терминалом),
  впишите команду pip install -r requirements.txt
- Пропишите в терминал python manage.py runserver, перейдите по ссылке http://127.0.0.1:8000/
  ### Формат для ввода ссылки - https://<домен> или http://<домен>


### Если вы используете Linux:
- Перейдите в папку с проектом (пример: cd projects/url-shortener)
- Создайте виртуальное окружение, для этого понадобится вписать команду python3 -m venv venv 
- Далее понадобится активировать виртуальное окружение, для этого пропишите source venv/bin/activate
- Установите зависимости командой pip install -r requirements.txt
- Запустите сервер с помощью команды python manage.py runserver, перейдите по ссылке http://127.0.0.1:8000/
  ### Формат для ввода ссылки - https://<домен> или http://<домен>

### Если вы используете Windows:
- Перейдите в папку с проектом (пример: cd projects/url-shortener)
- Создайте виртуальное окружение, для этого понадобится вписать команду python -m venv venv 
- Далее понадобится активировать виртуальное окружение, для этого пропишите venv\Scripts\activate.bat
- Установите зависимости командой pip install -r requirements.txt
- Запустите сервер с помощью команды python manage.py runserver, перейдите по ссылке http://127.0.0.1:8000/
  ### Формат для ввода ссылки - https://<домен> или http://<домен>
