import time


# Декоратор объявляется до декорируемой функции.
def time_of_function(func):
    # В декораторе должна быть вложенная функция.
    def wrapper():
        start_time = time.time()
        print('Время пошло')
        result = func()
        execution_time = round(time.time() - start_time, 1)
        print(f'Через {execution_time} сек. функция вернула «{result}»')
        return result
    # Нельзя вернуть строку, число или другой "невызываемый" объект.
    return wrapper


# Имя функции-декоратора (с символом @)
# ставится перед объявлением декорируемой функции.
@time_of_function
def sleep_one_sec():
    time.sleep(1)
    return 'Результат первой функции'


# После декорирования любой вызов функции sleep_one_sec()
# будет автоматически сопровождаться измерением времени её выполнения.
sleep_one_sec()
