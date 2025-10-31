def validate_the_status_code(response_code):
    if response_code == 200:
        print("Request is success")
    else:
        print("Request is failure")

validate_the_status_code(404)
validate_the_status_code(200)
validate_the_status_code(response_code=200)
validate_the_status_code(int(input("Enter the status code:")))