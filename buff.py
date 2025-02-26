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

    def get(self) -> int:
        return self._tape[self._cursor]


    def get(self,number: int) -> None:
        self._tape[self._cursor] = number


