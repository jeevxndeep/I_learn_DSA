def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n -i  -1):
            if arr[j] > arr[j + 1]:
               arr[j], arr[j + 1] = arr[j + 1], arr[j]

def radixsortwithbubblesort(arr):
    maxVal = max(arr)
    exp = 1

    while maxVal // exp > 0:
        radixArray =[[],[],[],[],[],[],[],[],[],[],]

        for num in arr:
            radixIndex = (num//exp) % 10
            radixArray[radixIndex].append(num)

        for bucket in radixArray:
            bubblesort(bucket)

        i = 0
        for bucket in radixArray:
            for num in bucket:
                arr[i] = num
                i += 1
        
        exp *= 10

myArray =[170, 45, 75, 90, 802, 24, 2, 66]
print('Original array:', myArray)
radixsortwithbubblesort(myArray)
print('Sorted array:', myArray)    
            





