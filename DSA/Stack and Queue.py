#### 1. Stack (LIFO – Last In First Out)
# - **Core operations**:
#   - `push(item)` → add to top
#   - `pop()` → remove from top
#   - `peek()` → see top without removing
#   - `is_empty()`
# - **Time complexity**: All O(1) when using `list.append()` and `list.pop()`

# **Real-life applications**:
#   - Undo/Redo in text editors
#   - Browser back/forward
#   - Function call stack in programming

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop() if self.items else None
    
    def peek(self):
        return self.items[-1] if self.items else None
    
    def is_empty(self):
        return len(self.items) == 0
    
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)

print("stack items :", s.items)
print("top item :", s.peek())
s.pop()
print("stack items :", s.items)
print("top item :", s.peek())
print("Is Empty ? = ", s.is_empty())
    

#### 2. Queue (FIFO – First In First Out)
# - **Core operations**:
#   - `enqueue(item)` → add to end
#   - `dequeue()` → remove from front
#   - `peek()` → see front without removing
#   - `is_empty()`
# - **Time complexity**: O(1) for `deque.append()` and `deque.popleft()`
# - **Real-life applications**:
#   - Task scheduling
#   - Printer jobs
#   - Ticket booking systems
print("")
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        self.items.append(item)
        
    def dequeue(self):
        return self.items.popleft() if self.items else None
        
    def peek(self):
        return self.items[0] if self.items else None
    
    def is_empty(self):
        return len(self.items) == 0
    
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

print("enqueue items : ", q.items)
print("Peek : ", q.peek())
q.dequeue()
print("enqueue items : ", q.items)
print("Peek : ", q.peek())
print("Is Empty ? = ", s.is_empty())
