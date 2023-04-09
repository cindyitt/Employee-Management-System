import sqlite3

# Connecting to the database
connection = sqlite3.connect('employee.db')

# Create a cursor object
cursor = connection.cursor()

# Creating a table to store the employee information
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        address TEXT,
        salary REAL
    )
''')

# Define a function to add an employee to the database
def add_employee():
    first_name = input('Enter the employee first name: ')
    last_name = input('Enter the employee last name: ')
    address = input('Enter the employee address: ')
    salary = float(input('Enter the employee salary: '))
    cursor.execute('INSERT INTO employees (first_name, last_name, address, salary) VALUES (?, ?, ?, ?)', (first_name, last_name, address, salary))
    connection.commit()
    print('The employee was added successfully \n')

# Function to remove an employee from the database
def remove_employee():
    id = int(input('Enter the employee ID: '))
    cursor.execute('DELETE FROM employees WHERE id = ?', (id,))
    connection.commit()
    print('The employee was removed successfully \n')

# Function to update an employee's information in the database
def update_employee():
    id = int(input('Enter the employee ID: '))
    first_name = input('Enter the employee first name: ')
    last_name = input('Enter the employee last name: ')
    address = input('Enter the employee address: ')
    salary = float(input('Enter the employee salary: '))
    cursor.execute('UPDATE employees SET first_name = ?, last_name = ?, address = ?, salary = ? WHERE id = ?', (first_name, last_name, address, salary, id))
    connection.commit()
    print('The employee was updated successfully \n')

# Function to search for employees in the database
def search_employee():
    name = input('Enter the employee name: ')
    cursor.execute('SELECT * FROM employees WHERE first_name LIKE ? OR last_name LIKE ?', ('%' + name + '%', '%' + name + '%'))
    rows = cursor.fetchall()
    if len(rows) == 0:
        print('No employees found')
    else:
        for row in rows:
            print(row)

# Function to display all employees in the database
def display_employees():
    cursor.execute('SELECT * FROM employees')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Function to display a menu options on the screen
def display_menu():
    print('Employee Management System:')
    print('1. Add Employee')
    print('2. Remove Employee')
    print('3. Update Employee')
    print('4. Search for Employee')
    print('5. Display All Employees')
    print('6. Exit')

# Main program
while True:
    display_menu()
    choice = int(input('Enter your choice from the menu: '))
    if choice == 1:
        add_employee()
    elif choice == 2:
        remove_employee()
    elif choice == 3:
        update_employee()
    elif choice == 4:
        search_employee()
    elif choice == 5:
        display_employees()
    elif choice == 6:
        break
    else:
        print('Invalid choice')

# Close the cursor and database connection
cursor.close()
connection.close()
