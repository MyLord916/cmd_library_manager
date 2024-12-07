class Book:
    def __init__(self, title: str, author: str, year: str):
        self.title = title
        self.author = author
        self.year = year


def format_book(book: object) -> dict:
    """Компоновка элементов книги для добавления в словарь"""
    data_book = {
        'title': book.title.capitalize().strip(),
        'author': book.author.title().strip(),
        'year': book.year,
        'status': 'в наличии'
    }
    return data_book
