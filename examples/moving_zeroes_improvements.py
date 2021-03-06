'''
Input: a List of integers
Returns: a List of integers
'''
'''
what if we had a pointer that started at the beginning
and a pointer that started at the end
and they moved towards each other in the middle?

if the left pointer "sees" a zero and the right pointer "sees" a non-zero
swap

if the left sees a non-zero increment
if the right sees a zero increment
'''

def moving_zeroes(arr):
    # initialize a left and right pointer
    # left is 0
    # right is last index in arr

    # while left <= right:
        # if left points at a zero and right points at non-zero
            # swap left and right items in original arr
            # increment left
            # decrement right
        # else
            # if left is non-zero:
                # increment left
            # if right is zero:
                # decrement right

    return arr
    
'''
What can I do to avoid having nested loops or needing to slice the arrays?
What about the names of my variable names? Could those also be improved?
'''