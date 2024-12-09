import json

from src import storage, schemas, config


def add_book(book: object) -> str:
    """Добавление книг в базу"""
    data_book = schemas.format_book(book)
    try:    # Проверяем наличие файла books.json
        file = open(config.path)
    except IOError as e:
        book_id = 1
        with open(config.path, "w", encoding="utf-8") as file:                      # Добавление в список первой книги
            json.dump({book_id: data_book}, file, indent=4, ensure_ascii=False)     # после создания файла books.json
        return f'Книга занесена в список: {book_id} - {data_book['title']} {data_book['author']} {data_book['year']}\
{data_book['status']}'
    else:
        data = storage.collect_data()
        if data_book not in data.values():
            if len(data):
                book_id = str(int(max(data)) + 1)   # Добавление книги в уже созданный файл books.json
            else:
                book_id = 1
            data.update({book_id: data_book})
            storage.update_json(data)
            return f'Книга занесена в список: {book_id} - {data_book['title']} {data_book['author']} \
{data_book['year']} {data_book['status']}'
        else:
            return 'Элемент уже присутствует в списке'


def del_book(book_id: str) -> str:
    """Удаление книг из базы по идентификатору"""
    data = storage.collect_data()
    if book_id in data:
        remove_book = data[book_id]
        del data[book_id]
        storage.update_json(data)
        return f'Книга удалена из списка: {remove_book['title']} {remove_book['author']} {remove_book['year']}'
    else:
        return 'Данный номер отсутствует в списке'


def change_status(book_id, status) -> str:
    """Изменение статуса наличия или сдачи книги"""
    data = storage.collect_data()
    if book_id in data:
        if status == '0':
            data[book_id]['status'] = 'выдана'
        elif status == '1':
            data[book_id]['status'] = 'в наличии'
        storage.update_json(data)
        book = data[book_id]
        return f'Статус книги изменен: {book['title']} {book['author']} {book['year']} {book['status']}'
    else:
        return 'Книги с таким номером не существует'


def search_book(items: list[str]) -> dict:
    """Поиск совпадений в списке книг"""
    data = storage.collect_data()
    result = {key: value for key, value in data.items() if
              any(point.lower() in (el.lower() for el in value.values()) for point in items)}
    return result


def show_books(data: dict = None) -> str:
    """Вывод списка всех книг в таблице"""
    if data is None:
        data = storage.collect_data()
    if len(data):
        book_indent = max([len(el['title']) for el in data.values()])
        author_indent = max([len(el['author']) for el in data.values()])
        columns = '|'.join((
            'id',
            ' title'.ljust(book_indent + 2),
            ' author'.ljust(author_indent + 2),     # Формирование заголовков списка
            ' year ',
            '  status  '))
        separator = ('-' * len(columns))    # Разделитель между заголовком и строками списка

        lines = [columns, separator]
        for book_id, items in data.items():
            items = list(items.values())
            items[0] = items[0].ljust(book_indent)
            items[1] = items[1].ljust(author_indent)    # Формирование строк списка
            items[2] = items[2].rjust(4)
            items[3] = items[3].rjust(9)
            lines.append(' | '.join((book_id, *items)))
        return '\n'.join(lines)
    else:
        return 'Список пуст'
