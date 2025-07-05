class MyQueue:

    def __init__(self):
        self.Queue = []
        
    def push(self, x: int) -> None:
        self.Queue.append(x)

    def pop(self) -> int:
        temp=[]
        while(self.Queue):
            temp.append(self.Queue.pop())
        
        solve=temp.pop()

        while(temp):
            self.Queue.append(temp.pop())
        
        return solve
        
    def peek(self) -> int:
        temp=[]
        while(self.Queue):
            temp.append(self.Queue.pop())
        
        solve=temp.pop()

        temp.append(solve)

        while(temp):
            self.Queue.append(temp.pop())
        
        return solve
        

    def empty(self) -> bool:
        if len(self.Queue)==0:
            return True
        else:
            return False