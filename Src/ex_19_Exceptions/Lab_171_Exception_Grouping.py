#python 3.11
from exceptiongroup import ExceptionGroup

eg=ExceptionGroup("Multiple Exceptions",
                  [ValueError("Invalid value"),
                              TypeError("Type Error"),ZeroDivisionError("Can't div zero")])

def check_div(a):
    if a==0:
        raise eg