def BinarySearch(arr, low, high, x):
    if high >= low:
        mid = (low + high) // 2  # Corrected formula for mid-point calculation

        if arr[mid] == x:
            return mid  # If element is found, return the index
        elif arr[mid] > x:
            return BinarySearch(arr, low, mid - 1, x)  # Search left part of the array
        else:
            return BinarySearch(arr, mid + 1, high, x)  # Search right part of the array
    else:
        return -1  # Element is not present in the array

if __name__ == "__main__":
    arr = list(map(int, input("Enter your SORTED array of numbers with spaces: ").split()))
    N = len(arr)
    x = int(input("Enter the number you want to search for: "))

    result = BinarySearch(arr, 0, N - 1, x)

    if result == -1:
        print("Number not found in the array")
    else:
        print(x, "Number found in the array at index:", result + 1)  # Display position as 1-based index
