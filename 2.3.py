# month_list = ['winter', 'spring', 'summer', 'autumn']
# month_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
# month_isk = int(input("Введите месяц по номеру "))
# if month_isk ==1 or month_isk == 12 or month_isk == 2:
#         print(month_dict.get(1))
#         print(month_list[0])
# elif month_list == 3 or month_list == 4 or month_list ==5:
#     print(month_dict.get(2))
#     print(month_list[1])
# elif month_isk == 6 or month_isk == 7 or month_isk == 8:
#     print(month_dict.get(3))
#     print(month_list[2])
#
# elif month_isk == 9 or month_isk == 10 or month_isk == 11:
#     print(month_dict.get(4))
#     print(month_list[3])
# else:
#         print("Такого месяца не существует")

while True:
    user_month = input('Введите номер месяца от 1 до 12 -')
    if user_month.isdigit() and 0 <= int(user_month) <= 12:
        season_1 = ['зима', 'весна', 'лето', 'осень', 'зима']
        season_2 = {0: 'зима', 1: 'весна', 2: 'лето', 3: 'осень', 4: 'зима'}
        print(f'Список сезонов - {season_1[int(user_month) // 3]}\n Словарь сезонов - {season_2[int(user_month) // 3]}\n')
        break
    else:
        print('Ошибка!')