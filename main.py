from src import handler, config

if __name__ == '__main__':
    while True:
        answer = input()
        try:
            print()
            print(handler.handler(answer))
            print()
        except KeyboardInterrupt:
            break
        except Exception as ex:
            print(f'Error: {ex}')
