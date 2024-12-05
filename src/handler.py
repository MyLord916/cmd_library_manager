from src import managers
from src import schemas


def process_add(text: str) -> None:
    items = [el.strip() for el in text.split('/')]
    if len(items) == 3:
        if items[-1].isdigit() or '':
            managers.add_book(schemas.Book(*items))
        else:
            print('Год должен быть числом')
    else:
        print('Необходимо указать данные в формате title/author/year')


def process_dell(text: str) -> None:
    if len(text.split()) == 1 and text.isdigit():
        managers.del_book(text)
    else:
        print('Необходимо указать номер книги для ее удаления')


def process_stat(text: str) -> None:
    items = text.split()
    if len(items) == 2 and all(el.isdigit() for el in items):
        if not -1 < int(items[-1]) < 2:
            print('Статус может быть только: 1 - в наличии, 0 - выдана')
        else:
            managers.change_status(*items)
    else:
        print('Необходимо указать номер книги и статус: 1 - В наличии, 0 - выдана')


def handler_command(command: str, ending: str) -> None:
    commands = {
        'add': process_add,
        'del': process_dell,
        'stat': process_stat
    }
    if command in commands:
        commands[command](ending)
    else:
        print(f'Unknown command: {command}')


def handler(mes: str) -> None:
    mes = mes.strip()

    if any(mes.startswith(command) for command in ['add', 'del', 'stat']):
        try:
            command, *ending = mes.split()
            text = ' '.join(ending)
            handler_command(command, text)
        except Exception as e:
            print(f'Error processing command: {e}')

    elif mes.startswith('all'):
        managers.show_books()

    else:
        managers.show_books(managers.search_book(*mes.split()))