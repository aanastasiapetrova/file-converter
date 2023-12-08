### Задача
	Необходимо разработать консольное приложение на языке Python для конвертирования и модификации данных из разных форматов в другие форматы.

## Конвертер файлов
### Цель
	Проверить знания построения архитектуры приложения, применения паттернов разработки.

### Техническое задание:
1. Приложение должно работать через консольную строку.
2. Приложение должно уметь принимать на вход различные параметры, опции и данные.
3. Функционал системы должен содержать следующие возможности:
    - читать аргументы командной строки
    - получать данные из разных источников (то есть в момент работы используется только один источник данных)
        + из файла
        + из удаленного url в Интернете
        + из файлового потока, переданного на вход приложения в консоли
    - уметь парсить данные из полученных данных 
        + из формата rss
        + из формата atom
        + из формата json
    - фильтровать/сортировать данные (эти опции могут быть переданы отдельно либо могут не передаваться)
        + сортировать по дате публикации (asc, desc)
        + брать 5 или 10 последних по дате публикации новостей
        + выделять новости конкретного автора
    - сохранять результат данных в разные форматы
        + в файл формата rss
        + в файл формата atom
        + в файл формата json
4. Код приложения должен быть покрыте тестами. Для тестирования использовать pytest.
5. Стиль кода должен быть проверен через ruff.

#### Пример использования
converter –input=https://lenta.ru/rss –output=rss.json –author=Иван Петров
