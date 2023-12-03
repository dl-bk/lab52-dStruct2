# Історія дій: Створіть клас Calculator, який
# використовує стек для зберігання операцій та
# операндів. Методи класу можуть виконувати операції,
# зберігаючи їх у стеці для подальшого відновлення
# історії обчислень.

class Stack:
    def __init__(self) -> None:
        self.stack = []
    
    def push(self, value):
                self.stack.append(value)
    
    def pop(self):
        if self.stack:
            item = self.stack.pop()
            return item
        else:
            print("stack is clear")
            return None
        
    def length(self):
        return len(self.stack)
    
    def isEmpty(self):
        return not bool(self.stack)

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None

class Calc(Stack):
    def __init__(self) -> None:
        super().__init__()
    
    def add(self, a, b):
         if isinstance(a, (float, int)) and isinstance(b, (int, float)):
              result = a + b
              data = [[a, self.add.__name__, b], result]
              self.push(data)
              return result
         else:
              raise ValueError("values must be numbers")
         
    def sub(self, a, b):
         if isinstance(a, (float, int)) and isinstance(b, (int, float)):
              result = a - b
              data = [[a, self.sub.__name__, b], result]
              self.push(data)
              return result
         else:
              raise ValueError("values must be numbers")
         
    def mul(self, a, b):
         if isinstance(a, (float, int)) and isinstance(b, (int, float)):
              result = a * b
              data = [[a, self.mul.__name__, b], result]
              self.push(data)
              return result
         else:
              raise ValueError("values must be numbers")
         
    def div(self, a, b):
         if b == 0:
              raise ZeroDivisionError("infinity")
         if isinstance(a, (float, int)) and isinstance(b, (int, float)):
              result = a / b
              data = [[a, self.div.__name__, b], result]
              self.push(data)
              return result
         else:
              raise ValueError("values must be numbers")
    


c = Calc()
c.add(3,5)
c.sub(5,3)
c.mul(5, 3)
c.div(6, 2)
print(c.peek())
c.pop()
print(c.peek())
c.pop()
print(c.peek())
c.pop()
print(c.peek())