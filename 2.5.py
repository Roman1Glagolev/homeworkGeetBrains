# my_list = [7, 5, 3, 3, 2]
# print(f"Рейтинг - {my_list}")
# digit = int(input("Введите число (111 - выход) "))
# while digit != 111:
#     for el in range(len(my_list)):
#         if my_list[el] == digit:
#             my_list.insert(el + 1, digit)
#             break
#         elif my_list[0] < digit:
#             my_list.insert(0, digit)
#         elif my_list[-1] > digit:
#             my_list.append(digit)
#         elif my_list[el] > digit and my_list[el + 1] < digit:
#             my_list.insert(el + 1, digit)
#     print(f"текущий список - {my_list}")
#     digit = int(input("Введите число "))

my_list = [7, 5, 3, 3, 2]
new_numbur = int(input("Введит еновый элемент рейтинга: "))
i = 0

for n in my_list:
    if new_numbur <= n:
        i += 1
my_list.insert(i, float(new_numbur))
print(my_list)