class MyQueue:

    def __init__(self):
        self.stack = []
        self.reverseStack = []
        
    
    def push(self, x: int) -> None:
        self.stack.append(x)
        
 
    def pop(self) -> int:
        while self.stack:
            self.reverseStack.append(self.stack.pop())

        if self.reverseStack:
            result = self.reverseStack.pop()

        while self.reverseStack:
            self.stack.append(self.reverseStack.pop())

        return result
        
    # 맨처음 값 리턴
    def peek(self) -> int:
        if self.stack:
            return self.stack[0]
        

    def empty(self) -> bool:
        if self.stack:
            return False
        else:
            return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()