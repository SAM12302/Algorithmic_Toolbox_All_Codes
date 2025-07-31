"""list1 = [5, 1, 3, 8, 11, 9]
n = len(list1)
min_value = list1[0]
for i in range(0, n):
    if list1[i] < min_value:
        min_value = list1[i]

print(list1)
print(min_value)"""

list1 = [5, 1, 3, 8, 11, 9]
n = len(list1)
minIndex = 0
for j in range(0, n - 1):
    minIndex = j
    for i in range(j + 1, n):
        if list1[i] < list1[minIndex]:
            temp = list1[minIndex]
            list1[minIndex] = list1[i]
            list1[i] = temp
            

print(list1)
print(minIndex)