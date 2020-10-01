def linear_search(arr, target):
    # Your code here

    # if target in arr:
    #     return arr.index(target)

    for i in range(0,len(arr)):
        if target == arr[i]:
            return i

    return -1   # not found


# print(linear_search([],-6))

# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    low = 0
    high = len(arr) - 1

    # check while low is less than or equal to high or not found
    while (low <= high):
        mid = (low + high)//2

        if target == arr[mid]:
            return mid

        # less than mid
        elif target < arr[mid]:
            high = mid - 1
            continue
        # greater than mid
        elif target > arr[mid]:
            low = mid + 1
            continue

    return -1  # not found


print(binary_search([-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9],12))