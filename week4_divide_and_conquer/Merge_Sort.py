def merge_sort(merge_list):
    if len(merge_list) <= 1:
        return merge_list
    n = len(merge_list)
    mid = n // 2
    left = merge_list[:mid]
    right = merge_list[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left_arr, right_arr):
    new = []
    i = 0
    j = 0
    l = len(left_arr)
    r = len(right_arr)
    while i < l and j < r:
        if left_arr[i] < right_arr[j]:
            new.append(left_arr[i])
            i = i + 1
        else:
            new.append(right_arr[j])
            j = j + 1
    new.extend(left_arr[i:])
    new.extend(right_arr[j:])
    return new

list1 = [4, 6, 2, 1, 10, 9, 11, 12]
sorted_list = merge_sort(list1)
print(sorted_list)