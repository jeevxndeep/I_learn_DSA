def binarysearch(arr, targetVal):
    left =  0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == targetVal:
            return mid
        if arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1
    return -1 

myArray = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
myTarget = 15

result = binarysearch(myArray, myTarget)

if result != -1:
    print('value', myTarget, 'found in index', result)
else:
    print('value',myTarget, 'not found')