def binary_search(arr, value):
    lo = 0
    hi = len(arr)-1

    while lo <= hi:
        mid = int((hi+lo)/2)
        if arr[mid] == value:
            print value,"found in the list at location",mid
            return mid
        elif arr[mid] < value:
            lo = mid+1
        else:
            hi = mid-1
    print value,"not found in the list"
    return False


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13]
    binary_search(arr, 8)
    binary_search(arr, 9)
