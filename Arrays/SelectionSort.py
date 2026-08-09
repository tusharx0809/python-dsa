"""Selection Sort"""

def selectionSort(arr: list[int]) -> None:
    size: int = len(arr)
    for i in range(0,size):
        min_idx: int = i
        for j in range(i+1, size):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[min_idx], arr[i] = arr[i], arr[min_idx]


def main():
    arr: list[int] = [5,1,6,2,3,8,7,9,0]
    selectionSort(arr)
    print(arr)

if __name__ == "__main__":
    main()