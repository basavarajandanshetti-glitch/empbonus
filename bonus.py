import sys
if len(sys.argv) == 2:
    salary = float(sys.argv[1])
    print("User provided salary value")
else:
    salary = 50000.0
    print("Default salary used")
bonus = salary * 0.10
total_salary = salary + bonus

print("Bonus Amount:", bonus)
print("Total Salary After Adding Bonus:", total_salary)
