import math
class MinStack:

    def __init__(self):
        self.stackVals = []
        self.stackMins = []

    def push(self, val: int) -> None:
        if len(self.stackVals) == 0:
            self.stackVals.append(val)
            self.stackMins.append(val)
        else:
            prevMin = self.stackMins[-1]
            self.stackVals.append(val)
            if val < prevMin:
                self.stackMins.append(val)
            else:
                self.stackMins.append(prevMin)

    def pop(self) -> None:
        self.stackVals.pop(-1)
        self.stackMins.pop(-1)

    def top(self) -> int:
        return self.stackVals[-1]

    def getMin(self) -> int:
        return self.stackMins[-1]
        
