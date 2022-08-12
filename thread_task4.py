import threading

summ = 0
lock = threading.Lock()


# 1 + 3 + 5..
def func(number, max1):
    sum1 = 0
    while True:
        sum1 += number
        if number == max1:
            break
        number += 2
    lock.acquire()
    global summ
    summ += sum1
    lock.release()


def main():
    thr = threading.Thread(target=func, args=(1, 5))
    thr2 = threading.Thread(target=func, args=(2, 4))
    thr.start()
    thr2.start()
    thr.join()
    thr2.join()
    print(summ)


if __name__ == '__main__':
    main()