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
    
    center = int(len(arr)/2)
    # print(center)
    # check center if matches return number

    if target == arr[center]:
        return 

        # if target > center cut right and repeat
    elif target > arr[center]:
        
        binary_search(arr[center:],target)

        # if target < center cut left and repeat
    else:
        binary_search(arr[:center],target)





    return -1  # not found


print(binary_search([-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9],1))