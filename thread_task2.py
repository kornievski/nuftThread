import threading
import time

MAX_N = 3 # Додатковий потік ... разів
DEMON_THREAD_WAIT_TIME = 1.3 # Додатковий потік із інтервалом у ... мс 
HEAD_THREAD_CHECK_TIME = .5 # Головний потік кожні ... мс перевіряє стан додаткового потоку
MESSAGE = "Hello world" # виводить у консоль ... 


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
