class Book:
    def __init__(self, items: list):
        try:
            self.title, self.author, self.year = items
        except ValueError:
            raise ValueError('Необходимо указать данные в формате title/author/year')


def format_book(book: object) -> dict:
    ''''''
    if not book.year.isdigit():
        raise ValueError('Год должен быть числом')
    data_book = {
        'title': book.title.capitalize().strip(),
        'author': book.author.title().strip(),
        'year': book.year,
        'status': 'в наличии'
    }
    return data_book


if __name__ == '__main__':
    print(format_book(Book(['Солнце живых', 'Шмелев И.', '1931'])))
