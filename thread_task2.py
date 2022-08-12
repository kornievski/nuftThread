import threading
import time

MAX_N = 3
DEMON_THREAD_WAIT_TIME = 1.3
HEAD_THREAD_CHECK_TIME = .5
MESSAGE = "Hello world"


def func():
    print(f'Додатковий потік почав роботу')
    for i in range(MAX_N):
        print(MESSAGE)
        time.sleep(DEMON_THREAD_WAIT_TIME)
    print(f'Додатковий потік завершився')


def main():
    thr = threading.Thread(target=func)
    thr.start()
    while True:
        if thr.is_alive():
            print('Потік живий')
            time.sleep(HEAD_THREAD_CHECK_TIME)
        else:
            print('Потік вмер')
            break


if __name__ == '__main__':
    main()