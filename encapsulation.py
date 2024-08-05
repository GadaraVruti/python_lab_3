class Calculator:
    def __init__(self,a,b):
        self._a=a
        self._b=b
    def add(self):
        return self._a+self._b
    def sub(self):
        return self._a-self._b
calc=Calculator(10,3)
print("Addition:",calc.add())
print("Subtraction:",calc.sub())