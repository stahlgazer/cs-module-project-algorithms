'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here
    products = []
    total = 1
    for i in range(len(arr)):
        # find total product of the list
        total = total * arr[i] 
        
    for i in range(len(arr)):
        # for each index, divide total by current index value
        products.append(int(total/arr[i])) 
                    
    return products

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
