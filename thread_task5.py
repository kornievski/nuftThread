import threading

summ = 0
lock = threading.Lock()


# 1 - 3 + 5 - 7..
def func(number, max_iterations, plus):
    sum1 = 0
    add = 0
    while True:
        if plus:
            sum1 += number
        else:
            sum1 -= number
        if add == max_iterations:
            break
        number += 4
        add += 1
    lock.acquire()
    global summ
    summ += sum1
    lock.release()


def main():
    thr = threading.Thread(target=func, args=(1, 3, True))
    thr2 = threading.Thread(target=func, args=(3, 3, False))
    thr.start()
    thr2.start()
    thr.join()
    thr2.join()
    print(summ)
    print(1-3+5-7+9-11+13-15)


if __name__ == '__main__':
    main()