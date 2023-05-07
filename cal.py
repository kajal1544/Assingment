class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Cannot divide by zero"
        else:
            return x / y

# Creating an object
calculator = Calculator()

#  Calculator operations
print("Addition: ", calculator.add(63,41))
print("Subtraction: ", calculator.subtract(55,3))
print("Multiplication: ", calculator.multiply(12,87))
print("Division: ", calculator.divide(5, 2))