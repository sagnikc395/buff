//  basically the buff interpreter is a brainfuck interpreter
//  that needs to support basic operations

//  1. keep track of the position. Go let and right on the tape, expanding
//  as needed and also removing empty(zero)cells on the left
//  2. Increment and decrement numbers at the current position
//  3. Determine whether the current cell is zero
//  4. input and output of the cells, to be used for input and output in the state machine

//  along with this we also need to check for the following:
//  1. Position must not go further left than 0.
//  2. Tape must be long enough for the current position
//  3. There may not be trailing zeros on the tape, except when the cursor is present
//  4. Cells must not be decremented to negative numbers

package main

import (
	"fmt"
)

// utilities
func pop(a []int) (int, []int) {
	return a[len(a)-1], a[:len(a)-1]
}

type InfiniteTape struct {
	tape   []int
	cursor int
}

func InitInfiniteType() *InfiniteTape {
	return &InfiniteTape{
		tape:   make([]int, 0),
		cursor: 0,
	}
}

func (it *InfiniteTape) Right() {
	it.cursor += 1
	if it.cursor == len(it.tape) {
		it.tape = append(it.tape, 0)
	}
}

func (it *InfiniteTape) Left() {
	if it.cursor == len(it.tape)-1 && it.IsZero() {
		_, new_arr := pop(it.tape)
		it.tape = new_arr
	}
	it.cursor -= 1
}

func (it *InfiniteTape) Increment() {
	it.tape[it.cursor] += 1
}

func (it *InfiniteTape) Decrement() {
	it.tape[it.cursor] -= 1
}

// utilities
func (it *InfiniteTape) IsZero() bool {
	return len(it.tape) == 0
}

func (it *InfiniteTape) Get() int {
	return it.tape[it.cursor]
}

func (it *InfiniteTape) Set(number int) {
	it.tape[it.cursor] = number
}

func main() {
	{
		fmt.Printf("Enter t1 and t2\n")
	}
}
