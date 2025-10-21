# Bucket Sort
# Time Complexity - Worst Case O(n^2) Best Case O(n+k)
# Space Complexity - O(n+k)


def bucket_sort(nums):
    
    n = len(nums)
    # Create n empty buckets.
    # Each slot in the array represents a bucket (list)
    # You have to create the list like this otherwise it points to the same list reference.
    buckets = [[] for _ in range(n)]
    # Insert every array[i] into bucket n*array[i].
    for number in nums:
        # Multiply each element by the number of buckets
        # Convert the result to an integer to remove the decimal
        # Clamp to n-1 so cant go out of range
        index = int(number * n, n - 1)
        # Insert the value into the index
        buckets[index].append(number)

    # Sort the elements within each bucket using insertion sort.
    for bucket in buckets:
        # In practice you would implement your own Insertion Sort or other Stable Sort
        bucket.sort()

    # Concatenate all sorted buckets.
    output_array = []
    for bucket in buckets:
        for item in bucket:
            output_array.append(item)
    
    return output_array  

nums = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
print("Un-sorted List: ", nums)
print("Sorted List: ", bucket_sort(nums))