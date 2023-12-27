## Конвертер файлов

***Задание:*** https://docs.google.com/document/d/1Ty5_mFR4MfGlqJfqlclIW2CoQXQXMyQwEWJGUovEKQM/edit

### Запуск проекта
1. Склонировать репозиторий на локальную машину
```
git clone git@github.com:aanastasiapetrova/file-converter.git
```
2. При помощи пакетного менеджера poetry активировать виртуальное окружение
```
poetry shell
```
3. Установить зависимости проекта
```
poetry install
```
4. Запустить команду конвертера файлов при помощи sh-скрипта
```
sh scripts/converter_file.sh <input> <output> <sort> <author> <limit>
```
5. Полный текст команды
```
python manage.py converter --input=<input value> --output=<output value> --sort=<sort value> --author=<author value> --limit=<limit value>
```

*Пример запуска команды для получения данных ***из файла*** с сортировкой новостей ***по возрастанию*** даты, фильрацией записей ***автора Brent Simmons*** и ограничением количества новостей в результирующей выборке до ***1*** объекта:*
```
python manage.py converter --input=tests/fixtures/test.json --output=test.rss --sort=asc --author=Brent Simmons --limit=1
```
или
```
sh scripts/converter_file.sh tests/fixtures/test.json test.rss asc "Brent Simmons" 1
```

*Пример запуска команды для получения данных ***по удаленному url*** с сортировкой новостей ***по убыванию*** даты, фильрацией записей ***автора Анна Щербакова*** и ограничением количества новостей в результирующей выборке до ***4*** объектов:*
```
python manage.py converter --input=http://lenta.ru/rss --output=test.atom --sort=desc --author=Анна Щербакова --limit=4
```
или
```
sh scripts/converter_file.sh http://lenta.ru/rss test.atom desc "Анна Щербакова" 4
```

*Пример запуска команды для получения данных ***через поток ввода*** с сортировкой новостей ***по убыванию*** даты, фильрацией записей ***автора Brent Simmons*** и ограничением количества новостей в результирующей выборке до ***1*** объектов:*
```
cat tests/fixtures/test.rss | python manage.py converter --input=stdin --output=test.json --sort=desc --author=Brent Simmons --limit=1
```
или
```
cat tests/fixtures/test.rss | sh scripts/converter_file.sh stdin test.json desc "Brent Simmons" 1
```