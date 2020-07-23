'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    # placeholder to store values
    winmax = [0] * (len(nums)-k+1)
    #loop through 
    for i in range(len(nums)-k+1):
        winmax[i] = nums[i]
        for j in range(i+1, i+k):     
            if winmax[i] < nums[j]:
                winmax[i] = nums[j]
    return winmax

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
