'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr, n):
    # Your code here
    # base case
    if n == 1:
        return 0

    i, temp = 1, 1

    # allocate memory for the product array
    prod = [1 for i in range(n)]    

    # initialize the product array as 1
    # loop, temp variable contains product of elements on left side 
    for i in range(n):
        prod[i] = temp
        temp *= arr[i]

    # initialize temp to 1 for product on right side
    temp = 1

    #loop, temp variable contains products of elements on right side
    for i in range(n-1, -1, -1):
        prod[i] *= temp
        temp *= arr[i]

    #print constructed product array
    for i in range(n):
        print(prod[i], end = " ")  

    return      
"""
    my_arr = [0] * len(arr)

    for i in range(0, len(arr)):
        copy = arr.copy()
        copy[i] = 1
        for val in copy:
            total = total * val
        my_arr[i] = total   

    return my_arr     
"""

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
