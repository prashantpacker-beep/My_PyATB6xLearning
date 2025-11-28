class InvalidException(Exception):
    pass
def can_you_drink(age):
    if age < 18:
        raise InvalidException("Invalid age of drinking")

    def check_zero_div(a):
        if a == 0:
            raise ZeroDivisionError("Can't divide the zero")

can_you_drink(20)