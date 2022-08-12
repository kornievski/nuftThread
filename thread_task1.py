import threading

MAX_N = 3
MAX_THREAD_DEMON = 3
MAX_THREAD_WITH_JOIN = 3


def func(number):
    print(f'Поток {number} почав роботу')
    for i in range(MAX_N):
        print(f'Номер потока {number} — працює')
    print(f'Поток {number} завершився')


def main():
    for i in range(MAX_THREAD_WITH_JOIN):
        thr = threading.Thread(target=func, args=(i, ))
        thr.start()
        thr.join()
    for i in range(MAX_THREAD_DEMON):
        threading.Thread(target=func, args=(i+MAX_THREAD_WITH_JOIN, )).start()


if __name__ == '__main__':
    main()