emp_sal ={}
while True:
    name = input("Enter employee name (or 'no' to stop): ")
    if name.lower == 'no':
        break
    sal = float(input("Enter employee salary: "))
    emp_sal [name]= sal

print(emp_sal)