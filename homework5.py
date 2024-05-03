my_list = ['apple', 'banana', 'tomato', 'potato', 'peach']
print(f'List: {my_list}')
print(f'First element: {my_list[0]}')
print(f'Last element: {my_list[-1]}')
print(f'Sublist: {my_list[2:5]}')
my_list[2] = 'qiwi'
print(f'Modified list: {my_list}\n')

my_dict = {'apple': 'яблоко', 'banana': 'банан', 'orange': 'апельсин'}
print(f'Dictionary: {my_dict}')
print(f'Translation: {my_dict["orange"]}')
my_dict.update({'kiwi': 'киви'})
print(f'Modified dictionary: {my_dict}')
