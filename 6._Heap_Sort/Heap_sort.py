# Function to heapify a subtree rooted with node i which is an index in arr[]
def heapify(arr, n, i):
    largest = i       # Initialize largest as root
    left = 2 * i + 1  # left = 2*i + 1
    right = 2 * i + 2 # right = 2*i + 2

    # See if left child of root exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # See if right child of root exists and is greater than root
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        # Heapify the root
        heapify(arr, n, largest)

# Function to perform Heap Sort
def heap_sort(arr):
    n = len(arr)

    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

# Get the list of numbers from the user
user_input = input("Enter numbers separated by spaces: ")
# Convert the string input to a list of integers
arr = list(map(int, user_input.split()))

# Print the unsorted list
print("Unsorted list:", arr)
# Sort the list using Heap Sort
heap_sort(arr)
# Print the sorted list
print("Sorted list:", arr)
