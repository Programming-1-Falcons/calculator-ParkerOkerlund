operation = input("What mathematical operation?: ")

first = int(input("What is the first number?: "))
second = int(input("What is the second number?: "))










if operation == "add":
    answer = first + second
    operation = "+"
elif operation == "subtract":
    answer = first - second
    operation = "-"
elif operation == "divide":
    answer = first // second
    operation = "/"
elif operation == "multiply":
    answer = first * second
    operation = "*"
elif operation == "exponet":
    answer = first ** second
    operation = "**"

print(first ,  operation , second , "=" , answer)


