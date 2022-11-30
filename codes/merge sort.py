def merge_sort(array):
    if len(array) < 2:
        return array
    
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) or j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
    
    return result
#best case performance
# elements are already sorted
array = [i for i in range(1, 20)]

print(array)
# 20 ALREADY sorted elements need 18 iterations approx = n
print(merge_sort(array))
#output is =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
           #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]


#average case performance
import random
# elements are randomly shuffled
array = [i for i in range(1, 20)]
random.shuffle(array)
print(array)
# 20 shuffled elements need 324 iterations approx = n * n
print(merge_sort(array))

#output is =[14, 17, 8, 13, 19, 11, 16, 18, 7, 15, 12, 6, 2, 3, 9, 1, 5, 4, 10]
            #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

#Worst Case Performance:
# elements are reverse sorted
array = [i for i in range(1, 20)]
# reversing the array
array = array[::-1]

print(array)
# 20 REVERSE sorted elements need 324 iterations approx = n * n
print(merge_sort(array)) 

#output is = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
             #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
