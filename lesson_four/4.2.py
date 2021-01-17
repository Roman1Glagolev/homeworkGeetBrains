my_list = [14, 15, 17, 8, 9, 11, 3, 4, 6]
more_then = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]
print(more_then)