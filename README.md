## Описание проекта:
В проекте реализован Telegram bot для добавления новых сотрудников
ссылка на бота: https://t.me/fio_list_bot

## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/glebtorbin/reg-telegram-bot.git
```
```
cd reg-telegram-bot
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv
```
```
source venv/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Выполнить миграции:
```
alembic revision --autogenerate -m 'create tables'
alembic upgrade heads 
```
Создать грузчика и двороника:
```
python3 create_roles.py 
```
Запустить проект:
```
python3 app/bot.py
```
Перейти в телеграм для пользования:
```
https://t.me/fio_list_bot
```


### Над проектом работал:
Глеб Торбин

