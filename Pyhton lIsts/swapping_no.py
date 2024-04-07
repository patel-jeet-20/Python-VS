list1 =  [12, 35, 9, 56, 24]
l = len(list1)
print(f'Before Swapping:{list1}')
temp = list1[0]
list1[0] = list1[l-1]
list1[l-1] = temp

print(f'after swapping:{list1}')