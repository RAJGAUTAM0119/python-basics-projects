my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

modified_list = []
for i in range(1,len(my_list),2):
  item = my_list[i]
  modified_list.append(item)
print(modified_list)