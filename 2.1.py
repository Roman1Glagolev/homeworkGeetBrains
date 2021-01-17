# my_list = [12, None, -77, 'True', True, 9.5]
# def my_type(el):
#     for el in range(len(my_list)):
#         print(type(my_list[el]))
#     return
# my_type(my_list)

my_list = ['a', 2, 2.3, True, [2, 3, 4], None]
for ind, el in enumerate(my_list, 1):
    print(f"{ind}{el} - {type(el)}")

