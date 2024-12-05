from unittest.mock import patch, MagicMock
from unittest import TestCase, main
from src.handler import handler
import src


class TestHandler(TestCase):

    @patch('src.managers.add_book')
    # @patch('src.schemas.Book')
    def test_add_book(self, mock_add):
        # Подготовка данных
        message = "add Title/Author/111"
        mock_book = MagicMock(spec=src.schemas.Book)
        mock_book.title = 'Title'
        mock_book.author = 'Author'
        mock_book.year = '1111'
        mock_add.return_value = None

        # Вызов функции
        handler(message)

        # Проверка вызова функции add_book
        mock_add.assert_called_once_with(mock_book)

    @patch('src.managers.del_book')
    def test_del_book(self, mock_del):
        mock_del.return_value = None

        message = "del 1"

        handler(message)

        # Проверка вызова функции del_book
        mock_del.assert_called_once_with('1')

    @patch('src.managers.change_status')
    # @patch('src.storage.collect_data')
    # @patch('src.storage.update_json')
    def test_change_status(self, mock_change_status):
        message = "1 1"

        handler(message)

        # Проверка вызова функции change_status
        mock_change_status.assert_called_once_with('1', '1')

    @patch('src.managers.show_books')
    def test_show_all_books(self, mock_show):
        message = "all"

        handler(message)

        # Проверка вызова функции show_books для отображения всех книг
        mock_show.assert_called_once()

    @patch('src.managers.show_books')
    @patch('src.managers.search_book')
    def test_search_books(self, mock_search, mock_show):
        message = "search some keywords"

        handler(message)

        # Проверка вызова функции search_book и show_books
        mock_search.assert_called_once_with('search', 'some', 'keywords')
        mock_show.assert_called_once()


if __name__ == '__main__':
    main()
