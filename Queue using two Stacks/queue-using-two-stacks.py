#!/usr/bin/python3

class Stack:
    def __init__(self):
        self.stack = []
        
    def __str__(self):
        return str(self.stack)
    
    def __len__(self):
        return len(self.stack)
        
    def peek(self):
        return self.stack[len(self.stack)-1]
        
    def pop(self):
        return self.stack.pop()
    
    def push(self, x):
        self.stack.append(x)
        
    def swap(self, stack):
        for i in range(len(self.stack)):
            stack.push(self.stack.pop())
        
s1 = Stack()
s2 = Stack()

T = int(input())
for t in range(T):
    q = list(map(int, input().split(" ")))
    if q[0] == 1:
        s1.push(q[1])
    elif q[0] == 2:
        if len(s2) == 0:
            s1.swap(s2)
        s2.pop()
    else:
        if len(s2) == 0:
            s1.swap(s2)
        print(s2.peek())
