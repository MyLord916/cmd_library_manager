from unittest import TestCase, main
from os import remove
from src.tools_library_manager import *


class ToolLibManTest(TestCase):
    def test_add(self):
        s = [
            'Солнце живых/Шмелев И./1931',
            'Плутония/Обручев В./1915',
            'Мы/Замятин Е./1920',
            'Алые паруса/Грин А./1922',
            'Легенды и мифы Древней Греции/Кун Н./1922'
            ]
        for i in s:
            add_book(i)
        self.assertEqual(len(collect_data()), 5)
        with self.assertRaises(TypeError):
            add_book('Плутония/Обручев В./1915')
        with self.assertRaises(ValueError):
            add_book('')
            add_book('Плутония/Обручев В./тыщадевятсотпятнадцатый')

    def test_change_status(self):
        change_status('1 0')
        self.assertEqual(collect_data()['1']['status'], 'выдана')
        change_status('1 1')
        self.assertEqual(collect_data()['1']['status'], 'в наличии')
        with self.assertRaises(TypeError):
            change_status('two 1')
            change_status('2 one')
        with self.assertRaises(ValueError):
            change_status('')
            change_status('100 1')

    def test_dell(self):
        del_book('1')
        self.assertEqual(len(collect_data()), 4)
        with self.assertRaises(ValueError):
            del_book('')
            del_book('100')

    def test_id(self):
        add_book('Чапаев/Фурманов Д./1923')
        self.assertEqual(list(collect_data().keys())[-1], '6')

    def test_search(self):
        self.assertEqual(len(search_book("1922")), 2)
        remove('books.json')


if __name__ == '__main__':
    main()
