'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    n = len(nums)
    max = 0
    #initialize new array to append max values
    new_arr = []
    #loop through array, one by one
    for i in range (n - k + 1):
        #then current while equal the current index in array
        max = nums[i]
        #loop through and compare numbers in array
        for j in range(1, k):
            #if the indexes added together are greater than the max
            if nums[i + j] > max:
                #then the new max would be the added indexes
                max = nums[i + j]
        #append the largest number to the new array
        new_arr.append(max)

    return new_arr




if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
