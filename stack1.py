# Реалізуйте клас стека роботи з цілими значеннями
# (стек цілих). Стек має бути фіксованого розміру.
# Реалізуйте набір операцій для роботи зі стеком
# o розміщення цілого значення у стеку;
# o виштовхування цілого значення зі стеку;
# o підрахунок кількості цілих у стеку;
# o перевірку, чи порожній стек;
# o перевірку, чи повний стек;
# o очищення стеку;
# o отримання значення без виштовхування
# верхнього цілого в стеку.
#  На старті додатка відобразіть меню, в якому
# користувач може вибрати необхідну операцію.

class Stack:
    def __init__(self, capacity) -> None:
        self.stack = []
        self.capacity = capacity

    def push(self, value):
        if len(self.stack) < self.capacity:
            if isinstance(value, int):
                self.stack.append(value)
            else:
                raise ValueError("Incorrect value")
        else:
            raise Exception("stack is full")
    
    def pop(self):
        if self.stack:
            item = self.stack.pop()
            return item
        else:
            print("stack is already clear")
            return None
        
    def length(self):
        return len(self.stack)
    
    def isEmpty(self):
        return not bool(self.stack)
    def isFull(self):
        return len(self.stack) == self.capacity
    
    def clear(self):
        self.stack = []

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None

stack_capacity = 5
stack = Stack(stack_capacity)
for i in range(stack_capacity):
    stack.push(i)

print(stack.peek())

print(stack.peek())
print(stack.isEmpty())
print(stack.isFull())
stack.clear()
print(stack.peek())