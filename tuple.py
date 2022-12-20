my_info = ('blaize', 21, 'uneployed')




print(my_info[0])


name,age,occuoation = my_info
print(name)
print(age)
print(occuoation)


one_element_tuple = (4,) #trailing comma 
print('\n')

numbers = [0, 254, 2, 6,6,6,6,-1, 3,8,6,6]

for num in numbers:
  if (num < 0):
   
    print("Negative number detected!")
    break
  print(num)
  big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

# Print only positive numbers:
for i in big_number_list:
  if i < 0:
    continue
  print(i)

