class Student:
    def __init__(self, number, name, courses):
        self.number = number
        self.name = name
        self.courses = courses
        self.inversion_count = 0


def merge_sort(arr, low, high):
    if low >= high:
        return 0 

    mid = (low + high) // 2
    inv = merge_sort(arr, low, mid)
    inv += merge_sort(arr, mid + 1, high)
    inv += count_inversions(arr, low, mid, high)

    return inv


def count_inversions(arr, low, mid, high):
    temp = [0] * len(arr)
    inv = 0
    i, j, k = low, mid + 1, low

    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            inv += (mid - i + 1)
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= high:
        temp[k] = arr[j]
        j += 1
        k += 1

    for i in range(low, high + 1):
        arr[i] = temp[i]

    return inv


def main():
    students = []
    inversion_count_map = {}

    csv_file = "students_unsorted.csv"

    # Reading the CSV file and creating student objects
    try:
        with open(csv_file, 'r') as file:
            next(file)  # Skip the header
            for line in file:
                values = line.strip().split(",")
                number = values[0]
                name = values[1]
                courses = list(map(int, values[2:]))
                students.append(Student(number, name, courses))
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    for student in students:
        student.inversion_count = merge_sort(student.courses, 0, len(student.courses) - 1)
        inversion_count_map[student.inversion_count] = inversion_count_map.get(student.inversion_count, 0) + 1

    print(f"Among the {len(students)} students:")

    for count, frequency in inversion_count_map.items():
        print(f"Students with {count} course code inversions are {frequency}")


if __name__ == "__main__":
    main()