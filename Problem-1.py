# Problem-1.py
# Language: Python 3
# Simple Calculator using a class
# Inputs: a (float), b (float), operation (string: "add","sub","mul","div" or "+","-","*","/")

class Calculator:
    def __init__(self, a: float, b: float):
        self.a = float(a)
        self.b = float(b)

    def add(self) -> float:
        return self.a + self.b

    def subtract(self) -> float:
        return self.a - self.b

    def multiply(self) -> float:
        return self.a * self.b

    def divide(self):
        if self.b == 0.0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return self.a / self.b

def run():
    print("Calculator (enter 'q' to quit). Example inputs: 3.5 2.0 add")
    while True:
        s = input("Enter a b operation: ").strip()
        if not s or s.lower() == 'q':
            break
        try:
            parts = s.split()
            if len(parts) != 3:
                print("Please enter exactly three values: a b operation")
                continue
            a_str, b_str, op = parts
            a = float(a_str); b = float(b_str)
            calc = Calculator(a, b)
            op = op.lower()
            if op in ("add", "+"):
                print(calc.add())
            elif op in ("sub", "subtract", "-"):
                print(calc.subtract())
            elif op in ("mul", "multiply", "*"):
                print(calc.multiply())
            elif op in ("div", "divide", "/"):
                try:
                    print(calc.divide())
                except ZeroDivisionError as e:
                    print("Error:", e)
            else:
                print("Unknown operation. Use add/sub/mul/div or + - * /")
        except ValueError:
            print("Invalid numeric input. Please enter valid numbers.")
    print("Exiting calculator.")

if __name__ == "__main__":
    run()