import time
def my_Time(a):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = a(*args, **kwargs)
        time.sleep(2)
        t2 = time.time()
        print(f'{a.__name__} executed in {t2 - t1} sec')
        return result

    return wrapper

@my_Time
def Stepin(namber1,namber2):
    item1 = f"{namber1**namber2}"
    return item1


namber1 = int(input("Введите чесло 1: "))
namber2 = int(input("Введите чесло 2: "))
print(Stepin(namber1,namber2))
