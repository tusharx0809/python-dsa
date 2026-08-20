def quickSort(arr: list[int]) -> list[int]:

    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [ele for ele in arr[1:] if ele < pivot]
    right = [ele for ele in arr[1:] if ele >= pivot]
    return quickSort(left) + [pivot] + quickSort(right)


def main():
    arr = [5, 1, 6, 2, 3, 8, 7, 9, 0]
    sorted_arr = quickSort(arr)
    print(sorted_arr)


if __name__ == "__main__":
    main()