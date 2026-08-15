"""MERGE SORT"""

def merge(arr: list[int], left:int, mid:int, right: int) -> None:
    #print(f"arr: {arr}, left: {left}, mid: {mid}, right: {right}")
    n1: int = mid-left+1
    n2: int = right-mid
    #print("n1:", n1)
    #print("n2:", n2)
    l: list[int] = [arr[left+i] for i in range(0,n1)]
    r: list[int] = [arr[mid+1+i] for i in range(0,n2)]
    #print("l",l)
    #print("r",r)
    i,j,k = 0,0,left

    while i < n1 and j < n2:
        if l[i] < r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = l[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = r[j]
        j += 1
        k += 1

def mergeSort(arr: list[int], left: int, right: int) -> None:
    if left >= right:
        return
    mid: int = left + (right - left) // 2

    mergeSort(arr, left, mid)
    mergeSort(arr, mid+1, right)

    merge(arr,left,mid,right)


def main():
    arr: list[int] = [5,1,6,2,3,8,7,9,0]
    mergeSort(arr,0,len(arr)-1)
    print(arr)

if __name__ == "__main__":
    main()