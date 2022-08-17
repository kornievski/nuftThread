import ctypes
import threading
import time

MAX_N = 5 # Додатковий потік ... разів
DEMON_THREAD_WAIT_TIME = .3 # із інтервалом у ... мс 
HEAD_THREAD_WAIT_TIME = 5 # Головний потік кожні ... мс перевіряє стан додаткового потоку
MESSAGE = "Hello world" #виводить у консоль ... 


def func():
    print(f'Додатковий потік почав роботу')
    for i in range(MAX_N):
        print(MESSAGE)
        time.sleep(DEMON_THREAD_WAIT_TIME)
    print(f'Додатковий потік завершився')


def main():
    thr = threading.Thread(target=func)
    thr.start()
    time.sleep(HEAD_THREAD_WAIT_TIME)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thr.ident, ctypes.py_object(SystemExit))
    if res > 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(thr.ident, 0)
    if res == 1:
        print(f'Додатковий потік примусово завершений')


if __name__ == '__main__':
    main()
