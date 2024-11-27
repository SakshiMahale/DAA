import csv

def calculate_salaries(employees):
    # Base case: if there are no employees
    if not employees:
        return None, None, 0

    # Base case: if there's only one employee
    if len(employees) == 1:
        emp = employees[0]
        
        
        net_salary = emp['Gross Salary'] - emp['Deductions'] -emp['Income Tax'] #calculate Gross SALARIES of EMPLOYEES
        
        
        print(f"Employee ID: {emp['Employee ID']}, Name: {emp['Name']}, Gross Salary: {emp['Gross Salary']:.2f}, Net Salary: {net_salary:.2f}")
        emp['Net Salary'] = net_salary  # Store the net salary
        return emp, emp, net_salary  # Min and max are the same for one employee

    # Divide the list into two halves
    mid = len(employees) // 2
    left_employees = employees[:mid]
    right_employees = employees[mid:]

    # Conquer: Recursively calculate salaries for both halves
    min_left, max_left, total_left = calculate_salaries(left_employees)
    min_right, max_right, total_right = calculate_salaries(right_employees)

    # Combine results
    total_net_salary = total_left + total_right

    # Find the global min and max
    if min_left and (not min_right or min_left['Net Salary'] < min_right['Net Salary']):
        min_salary_employee = min_left
    else:
        min_salary_employee = min_right

    if max_left and (not max_right or max_left['Net Salary'] > max_right['Net Salary']):
        max_salary_employee = max_left
    else:
        max_salary_employee = max_right

    return min_salary_employee, max_salary_employee, total_net_salary

def process_employee_data(file_path):
    employees = []

    # Read the CSV file
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Convert values to appropriate types
            employee_id = int(row['Employee ID'])
            name = row['Name']
            base_salary = float(row['Base Salary'])
            hra=float(row['HRA'])
            bonus = float(row['Bonus'])
            deductions = float(row['Deductions'])
            income_tax=float(row['Income Tax'])

            #CALCULATE GROSS SALARY 
            gross_salary = base_salary + hra + bonus 

            # Append employee data to the list
            employees.append({
                'Employee ID': employee_id,
                'Name': name,
                'Gross Salary': gross_salary,
                'Deductions': deductions,
                'Income Tax': income_tax
            })

    return employees

# File path to the CSV
file_path = 'employees_data.csv'  # Change this to your CSV file path

# Process employee data
employees = process_employee_data(file_path)

# Calculate salaries and find min/max using divide and conquer
min_employee, max_employee, total_salaries = calculate_salaries(employees)

# Output minimum and maximum net salaries
print("\nEmployee with Minimum Net Salary:")
if min_employee:
    #calculating net salary
    min_net_salary = min_employee['Gross Salary'] - min_employee['Deductions'] -min_employee['Income Tax']
    min_employee['Net Salary'] = min_net_salary  # Store the net salary
    print({**min_employee, 'Net Salary': min_net_salary})

print("\nEmployee with Maximum Net Salary:")
if max_employee:
    max_net_salary = max_employee['Gross Salary'] - max_employee['Deductions'] -max_employee['Income Tax']
    max_employee['Net Salary'] = max_net_salary  # Store the net salary
    print({**max_employee, 'Net Salary': max_net_salary})


