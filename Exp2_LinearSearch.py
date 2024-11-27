def LinearSearch(arr, N, x):
    for i in range(0, N):
        if arr[i] == x:  # Compare the element at the current index
            return i  # Return the index if found
    return -1  # If not found, return -1 after the loop completes

if __name__ == "__main__":
    arr = list(map(int, input("Enter the elements of your array with spaces: ").split()))
    N = len(arr)
    x = int(input("Enter the element you wish to search in your array: "))

    result = LinearSearch(arr, N, x)

    if result == -1:
        print("The element is not present in the array.")
    else:
        print(f"{x} Element found at index number: {result}")
