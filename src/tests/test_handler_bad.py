from unittest.mock import patch
from unittest import TestCase, main
from src.handler import handler


class TestHandlerBad(TestCase):

    def test_add_none(self):
        self.assertEqual(handler('   add  '), 'Необходимо указать данные в формате title/author/year')

    def test_add_str_year(self):
        self.assertEqual(handler('   add  title / author  / year   '), 'Год должен быть числом')

    def test_del_none(self):
        self.assertEqual(handler('  del   '), 'Необходимо указать номер книги для ее удаления')

    def test_stat_none(self):
        self.assertEqual(handler('stat'), 'Необходимо указать номер книги и статус: 1 - В наличии, 0 - выдана')

    @patch('src.storage.update_json')
    @patch('src.storage.collect_data')
    def test_stat_incorrect(self, mock_collect_data, mock_update_json):
        mock_collect_data.return_value = {
            "1": {
                "title": "Title",
                "author": "Author",
                "year": "1111",
                "status": "в наличии"
            }
        }
        mock_update_json.return_value = None

        self.assertEqual(handler('stat 1 100'), 'Статус может быть только: 1 - в наличии, 0 - выдана')
        self.assertEqual(handler('stat 100 1'), 'Книги с таким номером не существует')


if __name__ == '__main__':
    main()
