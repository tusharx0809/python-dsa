"""QUICK SORT"""

def partition(arr: list[int], low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1
    for j in range(low,high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


def quickSort(arr: list[int], low: int, high: int)-> None:
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

def main():
    arr: list[int] = [5,1,6,2,3,8,7,9,0]
    quickSort(arr,0,len(arr)-1)
    print(arr)
    
if __name__ == "__main__":
    main()