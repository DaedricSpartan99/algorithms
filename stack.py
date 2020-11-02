class Stack: 
    def __init__(self, array = []):
        self.array = array

    def push(self, x):
        self.array.append(x)

    def pop(self):
        out = self.array[-1]
        del self.array[-1]
        return out

    def top(self):
        return self.array[-1]

    def __len__(self):
        return len(self.array)
