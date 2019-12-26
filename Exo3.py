import numpy as np

def sort(arr):
    for i in range(len(arr)):
        lowest = arr[i]
        lowest_idx = i
        for j in range(i, len(arr)):
            if arr[j] < lowest:
                lowest_idx = j
                lowest = arr[j]
        arr[lowest_idx] = arr[i]
        arr[i] = lowest
    return arr

def dicho_search(arr, target, a, b):
    mid = int((a+b)/2)
    if target == arr[mid]:
        return mid
    if target < arr[mid]:
        return dicho_search(arr, target, a, mid)
    else:
        return dicho_search(arr, target, mid, b)

def divide_and_conquer(arr, target):
    idx0 = 0
    idx1 = int(len(arr)/8)
    results = []
    for i in range(8):
        tmp = arr[idx0:idx1]
        results.append(find_number(tmp, target, counter, int(len(arr)/8)))
        idx0 = idx1
        idx1 += int(len(arr)/8)

    for i in range(len(results)):
        if (results[i] != -1):
            return results[i]+i*int(len(arr)/8)

def find_number(arr, target, counter, value):
    for i in range(len(arr)):
        if (arr[i] == target):
            return i
    return -1

arr = np.arange(100)
np.random.shuffle(arr)
arr = list(arr)
print(arr)

counter = 0

value = 16

#QUESTION 1
print("\ngreedy algo")
while arr[counter] != value:
    counter+=1

print("index : " + str(counter))
print("value : " + str(arr[counter]))

#QUESTION 2
print("\n\ndivide and conquer\nIndex of value we are searching for :")
print(divide_and_conquer(arr, 16))

#QUESTION 3
print("\n\nDichotomy :\nsorted array :")
print(sort(arr))
print("index of value we are searching for :")
print(dicho_search(arr, value, 0, len(arr)))


