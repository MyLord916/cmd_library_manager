from unittest import TestCase, main
from os import remove

from src import managers as ma
from src import schemas as sc
from src import storage as st


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
            ma.add_book(sc.Book(*i.split('/')))
        self.assertEqual(len(st.collect_data()), 5)
        self.assertEqual(ma.add_book(sc.Book('Плутония', 'Обручев В.', '1915')), 'Элемент уже присутствует в списке')

    def test_change_status(self):
        self.assertEqual(ma.change_status('1', '0'), 'Статус книги изменен: Солнце живых Шмелев И. 1931 выдана')
        self.assertEqual(st.collect_data()['1']['status'], 'выдана')
        self.assertEqual(ma.change_status('1', '1'), 'Статус книги изменен: Солнце живых Шмелев И. 1931 в наличии')
        self.assertEqual(st.collect_data()['1']['status'], 'в наличии')
        self.assertEqual(ma.change_status('100', '1'), 'Книги с таким номером не существует')

    def test_dell(self):
        self.assertEqual(ma.del_book('1'), 'Книга удалена из списка: Солнце живых Шмелев И. 1931')
        self.assertEqual(len(st.collect_data()), 4)
        self.assertEqual(ma.del_book('100'), 'Данный номер отсутствует в списке')

    def test_id(self):
        ma.add_book(sc.Book('Чапаев', 'Фурманов Д.', '1923'))
        self.assertEqual(list(st.collect_data().keys())[-1], '6')

    def test_search(self):
        self.assertEqual(len(ma.search_book(["1922"])), 2)
        remove('books.json')


if __name__ == '__main__':
    main()
