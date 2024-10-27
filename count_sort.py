def counting_sort(arr):
    # Find the maximum element in the array
    max_val = max(arr)
    
    # Initialize a count array with zero values
    count = [0] * (max_val + 1)
    
    # Store the count of each element
    for num in arr:
        count[num] += 1

    # Rebuild the sorted array
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])

    return sorted_arr

# Example usage
arr = [435, 12, 342, 28, 13, 23, 10]
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)
