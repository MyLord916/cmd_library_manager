from src import managers
from src import schemas


def process_add(text: str) -> str:
    """"""
    items = [el.strip() for el in text.split('/')]
    if len(items) == 3:
        if items[-1].isdigit() or '':
            return managers.add_book(schemas.Book(*items))
        else:
            return 'Год должен быть числом'
    else:
        return 'Необходимо указать данные в формате title/author/year'


def process_dell(text: str) -> str:
    """"""
    if len(text.split()) == 1 and text.isdigit():
        return managers.del_book(text)
    else:
        return 'Необходимо указать номер книги для ее удаления'


def process_stat(text: str) -> str:
    """"""
    items = text.split()
    if len(items) == 2 and all(el.isdigit() for el in items):
        if not 0 <= int(items[-1]) <= 1:
            return 'Статус может быть только: 1 - в наличии, 0 - выдана'
        else:
            return managers.change_status(*items)
    else:
        return 'Необходимо указать номер книги и статус: 1 - В наличии, 0 - выдана'


def handler_command(command: str, ending: str) -> str:
    """"""
    commands = {
        'add': process_add,
        'del': process_dell,
        'stat': process_stat
    }
    if command in commands:
        return commands[command](ending)
    else:
        return f'Unknown command: {command}'


def handler(message: str) -> str:
    """Обработка ввода от пользователя"""
    message = message.strip()

    if any(message.startswith(command) for command in ['add', 'del', 'stat']):
        try:
            command, *ending = message.split()
            text = ' '.join(ending)
            return handler_command(command, text)
        except Exception as e:
            return f'Error processing command: {e}'

    elif message.startswith('all'):
        return managers.show_books()

    else:
        return managers.show_books(managers.search_book(message.split()))
        # Если ввод был без команд производится поиск в списке
