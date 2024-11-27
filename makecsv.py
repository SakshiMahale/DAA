import csv
import random

def generate_student_data():
    names = [
        "John", "Sarah", "Michael", "Emma", "David", "Olivia", "Liam", "Charlotte", "Noah", "Ava",
        "Mia", "Ethan", "Isabella", "Logan", "Sophia", "Lucas", "Amelia", "Benjamin", "Evelyn", "James",
        "Abigail", "Henry", "Harper", "Alexander", "Emily", "William", "Sofia", "Elijah", "Grace", "Aiden",
        "Chloe", "Matthew", "Lily", "Jackson", "Zoe", "Daniel", "Aria", "Michael", "Elizabeth", "Sebastian",
        "Nora", "David", "Penelope", "Joseph", "Riley", "Samuel", "Hannah", "Owen", "Lillian", "Andrew",
        "Ellie", "Levi", "Scarlett", "Isaac", "Victoria", "Caleb", "Eleanor", "Ryan", "Samantha", "Dylan",
        "Luna", "Nathan", "Stella", "Christian", "Zoey", "Hunter", "Aurora", "Carter", "Lucy", "Eli",
        "Sadie", "Gabriel", "Willow", "Connor", "Savannah", "Adrian", "Alyssa", "Colton", "Naomi", "Lincoln",
        "Isla", "Christopher", "Elena", "Evan", "Autumn", "Asher", "Claire", "Jeremiah", "Laila", "Easton",
        "Kinsley", "Luke", "Paige", "Nicholas", "Julia", "Jordan", "Sophie", "Hudson", "Piper", "Aaron"
    ]

    student_data = []
    for i in range(1, 101):
        name = random.choice(names)  # Randomly select a name
        courses = [random.randint(1, 4) for _ in range(4)]  # Randomly generate course scores between 1 and 4
        student_data.append([i, name, *courses])

    return student_data

def create_csv():
    students = generate_student_data()
    header = ["number", "name", "course1", "course2", "course3", "course4"]
    csv_file = "students_unsorted.csv"

    # Writing to the CSV file
    try:
        with open(csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)  # Write the header
            writer.writerows(students)  # Write the student data
        print(f"CSV file '{csv_file}' created successfully.")
    except Exception as e:
        print(f"Error creating file: {e}")

if __name__ == "__main__":
    create_csv()
