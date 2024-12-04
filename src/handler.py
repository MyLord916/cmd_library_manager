from src.managers import add_book, del_book, change_status, search_book, show_books
from src.schemas import Book


def handler(mes):
    mes = mes.strip()
    commands = {
        'add': add_book,
        'del': del_book,
        'stat': change_status
    }
    if any(mes.startswith(command) for command in commands):
        try:
            command, *ending = mes.split()
            text = ' '.join(ending).strip()
            if command == 'add':
                items = ' '.join(ending).split('/')
                commands[command](Book(items))
            elif command == 'del':
                commands[command](text)
            elif command == 'stat':
                commands[command](text)
        except Exception as e:
            print(e)
    elif mes.startswith('all'):
        show_books()
    else:
        items = mes.split()
        show_books(search_book(items))


if __name__ == '__main__':
    pass