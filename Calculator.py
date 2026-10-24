def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

dictionary = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide}

def calculate():
    ce = "y"
    while ce == "y":
        n1 = float(input("Define n1: "))
        keep = "y"
        while keep == "y":
            operator = input("Select operation: ")
            if operator not in dictionary:
                print("Operation is not supported")
                continue
            n2 = float(input("Define n2: "))
            if operator == "/" and n2 == 0:
                print("Division by zero isn't valid operation!")
                continue
            result = dictionary[operator](n1,n2)
            n1 = result
            print(result)
            keep = input("Do you want to keep the result?: ")
        ce = input("Start again?: ")
calculate()

# Basic solution:

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
    
dictionary = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide}
ce = "y"
while ce == "y":
    n1 = float(input("Define n1: "))
    operator = input("Select operation: ")
    n2 = float(input("Define n2: "))
    result = dictionary[operator](n1,n2)
    print(result)
    proceed = input("Do you want to keep the results?: ")
    while proceed == "y":
        n1 = result
        operator = input("Select operation: ")
        n2 = float(input("Define n2: "))
        result = dictionary[operator](n1, n2)
        print(result)
        proceed = input("Do you want to keep the results?: ")
    ce = input("Do you want to start again?: ")
