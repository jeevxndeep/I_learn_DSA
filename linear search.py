def linearsearch(arr, targetArr):
    for i in range(len(arr)):
        if arr[i] == targetArr:
            return i
    return -1

arr = [3, 7, 2, 9, 5]
targetArr = 9

result = linearsearch(arr, targetArr)

if result != -1:
    print('value', targetArr, 'found at index', result)
else:
    print('value', targetArr, 'not found')
    
    
