# 🧩 1️⃣ Write a Function to Check Test Case Status

# Problem:

# Write a function check_status(status_code) that returns:

# "PASS" if status_code = 200

# "FAIL" if status_code = 400 or 500

# "UNKNOWN" otherwise

# Example Input & Output:

# print(check_status(200))   # PASS

# print(check_status(500))   # FAIL

# print(check_status(302))   # UNKNOWN

status_code =int(input("Enter the status code:"))


def check_status_code(status_code):
  match status_code:
    case 200:
     return "PASS"
    case 404:
        return "FAIL"
    case 500:
     return "FAIL"
    case _:
     return "UNKNOWN"
result = check_status_code(status_code)
print(result)
