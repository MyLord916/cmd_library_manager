from unittest import TestCase, main
from os import remove

from src import managers as ma
from src import schemas as sc
from src import storage as st
from src import handler as ha


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
            ma.add_book(sc.Book(i.split('/')))
        self.assertEqual(len(st.collect_data()), 5)
        with self.assertRaises(TypeError):
            ma.add_book(sc.Book(['Плутония', 'Обручев В.', '1915']))
        with self.assertRaises(ValueError):
            ma.add_book(sc.Book(['Плутония', 'Обручев В.', 'тыщадевятсотпятнадцатый']))
        # with self.assertRaises(TypeError):
            ma.add_book(sc.Book(['']))

    def test_change_status(self):
        ma.change_status('1 0')
        self.assertEqual(st.collect_data()['1']['status'], 'выдана')
        ma.change_status('1 1')
        self.assertEqual(st.collect_data()['1']['status'], 'в наличии')
        with self.assertRaises(TypeError):
            ma.change_status('two 1')
            ma.change_status('2 one')
        with self.assertRaises(ValueError):
            ma.change_status('')
            ma.change_status('100 1')

    def test_dell(self):
        ma.del_book('1')
        self.assertEqual(len(st.collect_data()), 4)
        with self.assertRaises(ValueError):
            ma.del_book('')
            ma.del_book('100')

    def test_id(self):
        ma.add_book(sc.Book(['Чапаев', 'Фурманов Д.', '1923']))
        self.assertEqual(list(st.collect_data().keys())[-1], '6')

    def test_search(self):
        self.assertEqual(len(ma.search_book(["1922"])), 2)
        remove('books.json')


if __name__ == '__main__':
    main()
