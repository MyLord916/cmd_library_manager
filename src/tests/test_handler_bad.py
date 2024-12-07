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

    # @patch('src.storage.collect_data')
    # @patch('src.storage.update_json')
    # def test_stat_incorrect(self, mock_collect_data, mock_update_json):
    #     mock_collect_data.return_value = {
    #         "1": {
    #             "title": "Title",
    #             "author": "Author",
    #             "year": "1111",
    #             "status": "в наличии"
    #         }
    #     }
    #     mock_update_json.return_value = None
    #
    #     handler('stat 1 100')
    #
    #     mock_collect_data.assert_called_once()
    #     mock_update_json.assert_called_once()


if __name__ == '__main__':
    main()
