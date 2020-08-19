'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    #base case
    count = 0

    # when the index is in the range of the array
    for i in range (len(arr)):
        # and the index does not equal 0
        if arr[i] != 0:
            #then switch the index's
            arr[count] = arr[i]
            #and keep iterating through by 1
            count += 1
    #while the count is less than the length of the array
    while count < len(arr):
        #then count is equal to 0
        arr[count] = 0
        #keep iterating through by 1
        count += 1
    
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")