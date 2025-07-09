# employee_file = open("employees.txt", "a")
#
# employee_file.write("\nJena - Manager")
#
# employee_file.close()

employee_file = open("employees.txt", "w")  # - overwrite on file

employee_file.write("\nJena - Manager")

employee_file.close()

employee_file = open("index.html", "w")  # - overwrite on file

employee_file.write("<p>This is HTML</p>")

employee_file.close()



