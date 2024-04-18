immutable_var = 1, 'something', True  # создаем кортеж
print(immutable_var)                  # выводим содержание кортежа в консоль
immutable_var[0] = 2                  # пытаемся изменить элемент кортежа
                                      # операция не возможна так как элементы кортежа
                                      # являются неизменяемыми
mutable_list = [1, 'something', False]
mutable_list[2] = True
print(mutable_list)
