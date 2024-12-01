from unittest import TestCase, main
from src.handler_library_manager import handler


class HandLibManTest(TestCase):
    def test_handler(self):
        self.assertEqual(handler('add наука - sten kily 1895'),
                         {'id': 1, 'book': 'наука ', 'author': ' sten kily', 'year': '1895', 'status': 'в наличии'})

        self.assertEqual(handler('add наука и техника-дмитрий нозаров 2012'),
                         {'command': 'add', 'book': 'Наука и техника', 'author': 'Дмитрий Нозаров', 'year': 2012})

        self.assertEqual(handler(''), 'Сообщение должно начинаться с команды: add, del, stat')

        self.assertEqual(handler('колобок народное творчество 0000'),
                         'Сообщение должно начинаться с команды: add, del, stat')

        self.assertEqual(handler('add трудовой Лагерь пришел в упадок -петр Слепой 1994'),
                         {'command': 'add', 'book': 'Трудовой лагерь пришел в упадок', 'author': 'Петр Слепой',
                          'year': 1994})


if __name__ == '__main__':
    main()
