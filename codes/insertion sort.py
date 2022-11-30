def insertion_sort(array):
    global iterations
    iterations = 0
    for i in range(1, len(array)):
        current_value = array[i]
        for j in range(i - 1, -1, -1):
            iterations += 1
            if array[j] > current_value:
                array[j], array[j + 1] = array[j + 1], array[j] # swap
            else:
                array[j + 1] = current_value
                break


#Best Case Performance:
# elements are already sorted
array = [i for i in range(1, 20)]

insertion_sort(array)
# 20 ALREADY sorted elements need 18 iterations approx = n
print(array)
print(iterations)

#output is = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
                       #18

#Average Case Performance:
import random
# elements are randomly shuffled
array = [i for i in range(1, 20)]
random.shuffle(array)

insertion_sort(array)
# 20 shuffled elements need 324 iterations approx = n * n
print(array)
print(iterations)

#output is =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
           #89       


#Worst Case Performance:
# elements are reverse sorted
array = [i for i in range(1, 20)]
# reversing the array
array = array[::-1]

insertion_sort(array)
# 20 REVERSE sorted elements need 324 iterations approx = n * n

print(array)
print(iterations)
#output is =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
              #171