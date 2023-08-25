# Write a Python Program to generate the employee details using Random module.
# Employee Details:
# Emp Id(1 to 9999) : Random Number
# Emp Location (Kormangala, HSR Layout, Ballary, Mumbai, Chennai, Nellore, Gurgon, Hyderabad) Choose any city from the list dynamically
# Emp salary (20,000 to 1,50,000) Random Number.
# Take Input from the commandline for how many employee details to print and generate the employee details with the above specified details.
# Display all the details using generators concepts, yield, next()


import random
def generate_employee_details(number_employees):
    cities = ["Kormangala","HSR Layout","Ballary","Mumbai","Chennai","Nellore","Gurgaon","Hyderabad"]

    for i in range(1, number_employees + 1):
        Emp_id = random.randint(1, 9999)
        Emp_salary = random.randint(20000, 150000)
        city = random.choice(cities)

        # print(Emp_id)
        # print(Emp_salary)
        # print(city)

        yield f"Emp Id: {Emp_id}, Location: {city}, Salary: {Emp_salary}" ####### formatted string

num_employees = int(input("Enter the number of employee details to generate: ")) #### input will be given as manually in command line

emp_details = generate_employee_details(num_employees)  ######## this is the generator function obj

for i in range(num_employees):
    emp=next(emp_details)
    print(emp)


'''
print(obj.__next__())    
print(obj.__next__())    
print(obj.__next__())    
print(obj.__next__())    
'''
