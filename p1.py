import os

# 🚨 1. SQL Injection Vulnerability
def authenticate_user(user_input):
    query = "SELECT * FROM users WHERE username = '" + user_input + "'"
    print("Executing query:", query)  # 🚨 Query concatenation issue

# 🚨 2. Hardcoded Secret Key
secret_key = "my_super_secret_key"  # 🚨 Should use environment variables instead

# 🚨 3. Command Injection
def execute_command(command):
    os.system(command)  # 🚨 Direct system command execution

# 🚨 4. Inefficient Loop
def inefficient_loop():
    result = []
    for i in range(10000):  # 🚨 Unoptimized looping
        result.append(i * 2)
    return result

# 🚨 5. Unused Variables
def calculate_square(x):
    square = x * x  # 🚨 Square is calculated but never returned
    unused_variable = 12345  # 🚨 Unused variable

# 🚨 6. Uncaught Exception
def risky_division(a, b):
    return a / b  # 🚨 No exception handling for ZeroDivisionError

# 🚨 7. Poor Code Formatting
def bad_format():print("This line is poorly formatted")  # 🚨 No indentation

# 🚨 8. Open File without Closing
def open_file_bad():
    file = open("test.txt", "w")  # 🚨 Missing proper file closure
    file.write("Hello World!")

# 🚨 9. No Input Validation
def process_input(data):
    print("Processing:", data)  # 🚨 No validation for input type

# 🚨 10. Recursive Function Without Base Case (Stack Overflow Risk)
def infinite_recursion(n):
    return infinite_recursion(n + 1)  # 🚨 No exit condition

if __name__ == "__main__":
    authenticate_user("admin")
    execute_command("ls")
    inefficient_loop()
    calculate_square(5)
    risky_division(10, 0)
    bad_format()
    open_file_bad()
    process_input("Some data")
    infinite_recursion(1)  # 🚨 Will crash due to infinite recursion
