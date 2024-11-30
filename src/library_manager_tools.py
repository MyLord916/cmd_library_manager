import json

default_path = 'books.json'

def handler(mes):
    commands = {
        'add': add_book,
        'del': del_book,
        'stat': change_status
    }
    # if not any(cmd in commands.split(', ') for cmd in unit):
    #     return f'Сообщение должно начинаться с команды: {commands}'
    unit = tuple(mes.split())
    command, *book_author, year = unit
    book_author = ' '.join(book_author)
    book, author = book_author.split('-')
    data = {
        'book': book.capitalize().strip(),
        'author': author.title().strip(),
        'year': year,
        'status': 'в наличии'
    }
    return commands['add'](data)


def get_id() -> str:
    ''''''
    with open(default_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        return str(int(max(data)) + 1)


def collect_data(path: str = default_path) -> dict:
    ''''''
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def update_json(data):
    ''''''
    with open(default_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def add_book(text: str) -> None:
    ''''''
    elem = tuple(text.split('/'))
    book, author, year = elem
    data_book = {
        'book': book.capitalize().strip(),
        'author': author.title().strip(),
        'year': year,
        'status': 'в наличии'
    }
    try:
        file = open(default_path)
    except IOError as e:
        with open(default_path, "w", encoding="utf-8") as file:
            json.dump({1: data_book}, file, indent=4, ensure_ascii=False)
    else:
        data = collect_data()
        if data_book not in data.values():
            data.update({get_id(): data_book})
            update_json(data)
        else:
            raise TypeError('Элемент уже присутствует в списке')


def del_book(book_id: str) -> None:
    ''''''
    data = collect_data()
    del data[book_id]
    update_json(data)


def search_book(point: str) -> dict:
    ''''''
    data = collect_data()
    return {key: value for key, value in data.items() if point in value.values()}


def show_books(data: dict = None) -> None:
    ''''''
    if data is None:
        data = collect_data()
    book_indent = max([len(el['book']) for el in data.values()])
    author_indent = max([len(el['author']) for el in data.values()])
    columns = '|'.join(('id', ' book'.ljust(book_indent + 2), ' author'.ljust(author_indent + 2), ' year ', ' status'))
    print(columns)
    print('-' * len(columns))
    for id, item in data.items():
        item = list(item.values())
        item[0] = item[0].ljust(book_indent)
        item[1] = item[1].ljust(author_indent)
        print(id, *item, sep=' | ')


def change_status(book_id: str, status: str = '0') -> None:
    ''''''
    data = collect_data()
    if status == '0':
        data[book_id]['status'] = 'выдана'
    elif status == '1':
        data[book_id]['status'] = 'в наличии'
    else:
        raise TypeError('Статус может быть только: 1-(в наличии), 0-(выдана)')
    update_json(data)


if __name__ == '__main__':
    pass