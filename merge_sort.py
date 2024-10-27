def merge_sort(arr):
    if len(arr) > 1:
        # Find the middle point
        mid = len(arr) // 2

        # Split the array into two halves
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive calls to divide the halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the two halves
        merge(arr, left_half, right_half)


def merge(arr, left_half, right_half):
    i = j = k = 0

    # Copy data to temp arrays left_half and right_half
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # Check if any elements were left in the left_half
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    # Check if any elements were left in the right_half
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

# Test the merge sort function
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)
merge_sort(arr)
print("Sorted array:", arr)