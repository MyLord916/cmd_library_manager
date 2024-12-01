from tools_library_manager import add_book, del_book, change_status, search_book, show_books


def handler(mes):
    commands = {
        'add': add_book,
        'del': del_book,
        'stat': change_status
    }
    pref, *text = mes.split()
    try:
        commands[pref](' '.join(text))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    pass
