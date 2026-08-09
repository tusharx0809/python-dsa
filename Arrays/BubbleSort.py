"""Bubble sort"""

def bubbleSort(arr: list[int]) -> None:
    size: int = len(arr)
    for i in range(0, size):
        swapped = False
        for j in range(0,size-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break



def main():
    arr: list[int] = [5,1,6,2,3,8,7,9,0]
    bubbleSort(arr)

    print(arr)

if __name__ == "__main__":
    main()