my_list = [1 , 3 , 7 , 3 , 4 , 8 , 5 , 8 , 8 , 1]
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)
unique_list.sort()
print(unique_list) 