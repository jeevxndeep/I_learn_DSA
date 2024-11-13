def countingsort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    sorted_arr = []

    for i in range(len(count)):
        while count[i] > 0:
            sorted_arr.append(i)
            count[i] -= 1

    return sorted_arr

unsortedArr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]    
sortedArr = countingsort(unsortedArr)
print('Sorted array:', sortedArr) 




