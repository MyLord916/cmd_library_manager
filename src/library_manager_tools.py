class Books:
    def __init__(self, book, author, year):
        self.id = None
        self.book = book
        self.author = author
        self.year = year
        self.status = None


def handler(mes: str) -> dict:
    unit = tuple(mes.split())
    commands = 'add, del, stat'
    if not any(cmd in commands.split(', ') for cmd in unit):
        return f'Сообщение должно начинаться с команды: {commands}'
    command, *book_author, year = unit
    book_author = ' '.join(book_author)
    print(book_author)
    book, author = book_author.split('-')
    res = {'command': command, 'book': book.capitalize().strip(), 'author': author.title().strip(), 'year': int(year)}
    return res


def add_book():
    pass


def del_book():
    pass


def search_book():
    pass


def show_books():
    pass


def change_status():
    pass


if __name__ == '__main__':
   pass