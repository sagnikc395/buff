'''
state machine
this takes a program and inputs and we can go and step through the program
we can just count the brackets and move within the programuntil we have
reached the matching bracket

'''

from typing import List

from .store import InfiniteTape

class StateMachine:
    def __init__(self,program: str,inputs: List[int]):
        self.program = program
        self.inputs = inputs
        self.tape = InfiniteTape()
        self.pc = 0
        self.outputs = []

        
    def goto_bracket(self,forward: bool):
        curr_bracket = ""
        target_bracket = ""
        increment = 0
        bracketCounter = 0
        if forward:
            curr_bracket ="["
            target_bracket = "]"
            increment =1
        else:
            curr_bracket = "]"
            target_bracket = "["
            increment = -1

        while True:
            instruction = self.program[self.pc]
            if instruction == curr_bracket:
                bracketCounter += 1
            elif instruction == target_bracket:
                bracketCounter -= 1
                if bracketCounter == 0 :
                    break

            self.pc += increment

    def step(self):
        instruction = self.program[self.pc]
        match instruction:
            case '+':
                self.tape.increment()
            case '-':
                self.tape.decrement()
            case '>':
                self.tape.right()
            case '<':
                self.tape.left()
            case ',':
                item = self.inputs.pop()
                self.tape.set(item)
            case '-':
                self.outputs.append(self.tape.get())
            case '[':
                if self.tape.is_zero():
                    self.goto_bracket(True)
            case ']':
                if not self.tape.is_zero():
                    self.goto_bracket(False) 

        self.pc += 1
        
