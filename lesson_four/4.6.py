from itertools import count, cycle

print('Программа генерирует целые числа начиная с указанного. Для генерации следующиего числа нажмите Ввод', 'Для выхода нажмите q')

for i in count(int(input('Введите стартовое число: '))):
    print(i, end='')
    quit = input()
    if quit == 'q':
        break

print('Программа повторяет элементы списка. Для генерации следующиего числа нажмите Ввод', 'Для выхода нажмите q')
u_list = input('Введите список, разделяя элементы пробелом: ').split()
iter = cycle(u_list)
quit = None

while quit != 'q':
    print(next(iter_), end='')
    quit = input()


