# my_list = ['a', 'b', 'c', 'd', 'e']
# if len(my_list) % 2 == 0:
#     i = 0
#     while i < len(my_list):
#         el = my_list[i]
#         my_list[i] = my_list[i+1]
#         my_list[i+1] = el
#         i += 2
# else:
#     i = 0
#     while i < len(my_list) - 1:
#         el = my_list[i]
#         my_list[i] = my_list[i + 1]
#         my_list[i + 1] = el
#         i += 2
# print(my_list)



list = input('Введите числа с пробелами - ').split()
for i in range(1, len(list), 2):
        list.insert(i - 1, list.pop(i))
print(list)








