class Calculator:
    #Calculator class
    def addition(self, a, b):
        #sum of a and b
        return a + b

    def subtraction(self, a, b):
        #subtraction of a and b
        return a - b

    def multiplication(self, a, b):
        #multiplication of a and b
        return a * b

    def division(self, a, b):
        #division of a and b
        if b == 0:
            raise ValueError("Cannot divide by zero. Choose another number.")
        return a / b