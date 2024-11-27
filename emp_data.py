import csv
import random
import faker

# Initialize Faker to generate random names
fake = faker.Faker()

# Number of employees
num_employees = 2000

# File path for the CSV file
file_path = 'employees_data.csv'

# Create employee data
employees = []
for employee_id in range(1, num_employees + 1):
    name = fake.name()
    base_salary = round(random.uniform(30000, 120000), 2)  # Base salary between 30k and 120k
    hra = round(base_salary * 0.20, 2)  # HRA as 20% of base salary
    bonus = round(random.uniform(2000, 10000), 2)  # Bonus between 2k and 10k
    deductions = round(random.uniform(1000, 5000), 2)  # Deductions between 1k and 5k
    income_tax = round((base_salary + hra + bonus - deductions) * 0.10, 2)  # 10% of taxable income

    employees.append({
        'Employee ID': employee_id,
        'Name': name,
        'Base Salary': base_salary,
        'HRA': hra,
        'Bonus': bonus,
        'Deductions': deductions,
        'Income Tax': income_tax
    })

# Write to CSV file
with open(file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=employees[0].keys())
    writer.writeheader()
    writer.writerows(employees)

print(f"CSV file '{file_path}' with {num_employees} employees created successfully.")
