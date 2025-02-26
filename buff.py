#/usr/bin/python

# basically the buff interpreter is a brainfuck interpreter
# that needs to support basic operations

# 1. keep track of the position. Go let and right on the tape, expanding
# as needed and also removing empty(zero)cells on the left
# 2. Increment and decrement numbers at the current position
# 3. Determine whether the current cell is zero
# 4. input and output of the cells, to be used for input and output in the state machine

# along with this we also need to check for the following:
# 1. Position must not go further left than 0.
# 2. Tape must be long enough for the current position
# 3. There may not be trailing zeros on the tape, except when the cursor is present
# 4. Cells must not be decremented to negative numbers


class InfiniteTape:
    def __init__(self) -> None:
        # tape is a just a long list of binary numbers
        self._tape = [0]
        self._cursor = 0

    def right(self) -> None:
        self._cursor += 1
        if self._cursor == len(self._tape):
            self._tape.append(0)

    def left(self) -> None:
        assert self._cursor > 0
        if self._cursor == len(self._tape) - 1 and self.is_zero():
            self._tape.pop()
        self._cursor -= 1

    def increment(self) -> None:
        self._tape[self._cursor] += 1

    def decrement(self) -> None:
        assert not self.is_zero()
        self._tape[self._cursor] -= 1

    def is_zero(self) -> int:
        return self.get() == 0 

    def get(self) -> int:
        return self._tape[self._cursor]

    def set(self,number: int) -> None:
        self._tape[self._cursor] = number

# state machine:
# this takes a program and inputs and we can go and step through the program

# we can just count the brackets and move within the program until we have reached the matching bracket

class StateMachine:
    def __init__(self,program: str, inputs: list[int]) -> None:
        self._program = program
        self._inputs = inputs
        self._tape = InfiniteTape()

        self._pc = 0
        self._outputs = []

    def run(self) -> list[int]:
        while self._pc != len(self._program):
            self.step()
        return self._outputs
    
    def _goto_bracket(self,forward: bool) -> None:
        curr_bracket = "[" if forward else "]"
        target_bracket = "]" if forward else "["

        increment = 1 if forward else -1
        bracket_counter = 0

        while True:
            instruction = self._program[self._pc]
            if instruction == curr_bracket:
                bracket_counter += 1
            elif instruction == target_bracket:
                bracket_counter -= 1
                if bracket_counter == 0:
                    break
            self._pc += increment

    def step(self) -> None:
        instruction = self._program[self._pc]
        match(instruction):
            case "+":
                self._tape.increment()
            case "-":
                self._tape.decrement()
            case ">":
                self._tape.right()
            case "<":
                self._tape.left()
            case ",":
                self._tape.set(self._inputs.pop(0))
            case ".":
                self._outputs.append(self._tape.get())
            case "[":
                if self._tape.is_zero():
                    self._goto_bracket(forward=True)
            case "]":
                if not self._tape.is_zero():
                    self._goto_bracket(forward=False)

        self._pc += 1
        
