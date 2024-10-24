"""
This function finds the position of an element in the rotated, sorted array and use search binary.
It takes to parameters: array, the list of elements
                        element, the target element to search in the array
"""
def search_rotated_sorted(array, element):
    # Initialize pointer to the binary search to keep track of the current intervals
    # low_index, points to the first element of the array
    # high_index, point to the last element of the array
    low_index = 0 
    high_index = len(array) - 1 

    # Perform the binary search within the current bound of low_index and high_index
    while low_index <= high_index: #  continue the binary search
        middle_index = (low_index + high_index) // 2 # Calculate the middle index for comparison
 
  
        # If the element at middle_index is same as the target element return its index
        if array[middle_index] == element:
            return middle_index
        
        # If the left half from low_index to middle_index is sorted.
        if array[middle_index] >= array[low_index]: # Left half sorted

            # Check if the target element is greater or equal to the low index and less to the middle index
            if element >= array[low_index] and element < array[middle_index]: 
                high_index = middle_index - 1 # Updated to be one position to the left of the middle index.
            else:
                low_index = middle_index + 1 # Updated to be one position to the right of the middle index.
        
        # Searching for the sorted elements in the right half
        else:
            if element > array[middle_index] and element <= array[high_index]: # Target element is greater than element in the middle index and less or equal to element in the high index
                low_index = middle_index + 1 # Updated to be one position to the right of the middle index.
            else:
                high_index = middle_index - 1 # Updated to be one position to the left of the middle index.
    
    return -1  # Target element not found, return -1

array = [35, 45, 55, 65, 75, 5, 10, 15, 25] 
element = 55
array2 = [35, 45, 55, 65, 75, 5, 10, 15, 25] 
element2 = 0 

# Display the results
print(search_rotated_sorted(array, element)) # Output, 2
print(search_rotated_sorted(array2, element2)) # Output, -1       
