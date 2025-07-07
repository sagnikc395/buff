'''
   basically the buff interpreter needs to do some basic operations

   1. keep track of the position. Go left and right on the tap, expanding as neede and also removing empty (zero) cells
   on the left
   2. increment and decrement numbers at the current position
   3. determine whether the current cell is zero
   4. input and output of the cells, to be used for input and output in the state machine 
'''


class InfiniteTape:
    def __init__(self):
        self.tape = [] 
        self.cursor = 0

    def right(self):
        self.cursor += 1
        if self.cursor == len(self.tape):
            self.tape.append(0)

    def left(self):
        if self.cursor == len(self.tape) -1 and self.is_zero():
            self.tape.pop()

        self.cursor -= 1

    def increment(self):
        self.tape[self.cursor] += 1

    def decrement(self):
        self.tape[self.cursor] -= 1

    def is_zero(self) -> bool:
        return len(self.tape) == 0

    def get(self) -> int:
        return self.tape[self.cursor]

    def set(self, number: int):
        self.tape[self.cursor] = number

        
