employee_file = open("employees.txt", "r") # reading and writing
# open("employees.txt", "w") # writing
# open("employees.txt", "a") # append
# open("employees.txt", "r+") # reading and writing

print(employee_file.readable())

# employee_file = open("employees.txt", "w") -> open file in write mode
# print(employee_file.writable()) -> is file writable

# print(employee_file.read()) 
# print(employee_file.readline())
# print(employee_file.readline())
# print(employee_file.readlines()[1])

for line in employee_file.readlines():
    print(line)



employee_file.close()