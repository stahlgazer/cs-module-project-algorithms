'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    if len(arr) > 0:
        arr.sort()
    for i in range(len(arr)):
        if i == 0:
            left = arr[i+1]
            right = arr[i+1]
        if i > 0 and i < len(arr) -1 :
            left = arr[i-1]
            right = arr[i+1]
        if i == len(arr)-1:
            right = arr[i-1]
            left = arr[i-1]
        if arr[i] != left and arr[i] != right:
            return arr[i]
        else: pass


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")

