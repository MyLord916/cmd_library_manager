import json

from src import config, storage, schemas, config


def add_book(book: object) -> None:
    ''''''
    data_book = schemas.format_book(book)
    try:
        file = open(config.path)
    except IOError as e:
        with open(config.path, "w", encoding="utf-8") as file:
            json.dump({1: data_book}, file, indent=4, ensure_ascii=False)
    else:
        data = storage.collect_data()
        if data_book not in data.values():
            if len(data):
                book_id = str(int(max(data)) + 1)
            else:
                book_id = 1
            data.update({book_id: data_book})
            storage.update_json(data)
        else:
            print('Элемент уже присутствует в списке')


def del_book(book_id: str) -> None:
    ''''''
    data = storage.collect_data()
    if book_id in data:
        del data[book_id]
        storage.update_json(data)
    else:
        print('Данный номер отсутствует в списке')


def change_status(book_id, status) -> None:
    ''''''
    data = storage.collect_data()
    if book_id in data:
        if status == '0':
            data[book_id]['status'] = 'выдана'
        elif status == '1':
            data[book_id]['status'] = 'в наличии'
    else:
        print('Книги с таким номером не существует')
    storage.update_json(data)


def search_book(*items: list[str]) -> dict:
    ''''''
    data = storage.collect_data()
    result = {key: value for key, value in data.items() if
              any(point.lower() in (el.lower() for el in value.values()) for point in items)}
    return result


def show_books(data: dict = None) -> None:
    ''''''
    if data is None:
        data = storage.collect_data()
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