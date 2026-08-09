"""Insertion Sort"""

def insertionSort(arr: list[int]) -> None:
    size = len(arr)
    for i in range(1,size):
        key = arr[i]
        j = i-1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key

arr = [5,1,6,2,3,8,7,9,0]
insertionSort(arr)
print(arr)