import json

from src.config import default_path
from src.storage import collect_data, update_json
from src.schemas import format_book, Book


def add_book(book: object) -> None:
    ''''''
    data_book = format_book(book)
    try:
        file = open(default_path)
    except IOError as e:
        with open(default_path, "w", encoding="utf-8") as file:
            json.dump({1: data_book}, file, indent=4, ensure_ascii=False)
    else:
        data = collect_data()
        if data_book not in data.values():
            if len(data):
                book_id = str(int(max(data)) + 1)
            else:
                book_id = 1
            data.update({book_id: data_book})
            update_json(data)
        else:
            raise TypeError('Элемент уже присутствует в списке')


def del_book(book_id: str) -> None:
    ''''''
    data = collect_data()
    if book_id.isdigit():
        if book_id in data:
            del data[book_id]
            update_json(data)
        else:
            raise ValueError('Данный номер отсутствует в списке')
    else:
        raise ValueError('Необходимо указать номер книги для ее удаления')


def change_status(text) -> None:
    ''''''
    try:
        book_id, status = text.split()
    except ValueError:
        raise ValueError('Необходимо указать номер книги и статус: 1 - В наличии, 0 - выдана')
    if book_id.isdigit():
        data = collect_data()
        if book_id in data:
            if status == '0':
                data[book_id]['status'] = 'выдана'
            elif status == '1':
                data[book_id]['status'] = 'в наличии'
            else:
                raise TypeError('Статус может быть только: 1 - в наличии, 0 - выдана')
        else:
            raise ValueError('Книги с таким номером не существует')
    else:
        raise TypeError('Для смены статуса нужно указать номер книги')
    update_json(data)


def search_book(items: list[str]) -> dict:
    ''''''
    data = collect_data()
    result = {key: value for key, value in data.items() if
              any(point.lower() in (el.lower() for el in value.values()) for point in items)}
    return result


def show_books(data: dict = None) -> None:
    ''''''
    if data is None:
        data = collect_data()
    if len(data):
        book_indent = max([len(el['title']) for el in data.values()])
        author_indent = max([len(el['author']) for el in data.values()])
        columns = '|'.join(
            ('id', ' title'.ljust(book_indent + 2), ' author'.ljust(author_indent + 2), ' year ', ' status'))
        print(columns)
        print('-' * len(columns))
        for id, item in data.items():
            item = list(item.values())
            item[0] = item[0].ljust(book_indent)
            item[1] = item[1].ljust(author_indent)
            print(id, *item, sep=' | ')
    else:
        print('Нет совпадений')


if __name__ == '__main__':
    show_books(search_book(['1922']))
