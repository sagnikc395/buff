import sys
# Assuming machine.py and store.py are in the same directory or importable path
from buff import machine

def main():
    """
    Main function to run the Brainfuck REPL.
    """
    print("Welcome to the Brainfuck REPL!")
    print("Enter your Brainfuck code. Type 'exit' to quit.")
    print("For inputs (',' instruction), enter comma-separated numbers when prompted.")
    print("Example: Code `+,` with Input `65` will set cell 0 to 65.")
    print("Example: Code `+++++++[>+++++++<-]>.` (Hello World part) will output 72.")

    while True:
        try:
            # Get Brainfuck program input from the user
            program_input = input("\nEnter Brainfuck code (or 'exit' to quit): ")
            if program_input.lower() == 'exit':
                print("Exiting REPL. Goodbye!")
                break

            # Get numeric inputs for the ',' instruction
            inputs_str = input("Enter inputs (comma-separated numbers, e.g., 65,66) or leave blank: ")
            inputs = []
            if inputs_str.strip():
                try:
                    inputs = [int(x.strip()) for x in inputs_str.split(',')]
                except ValueError:
                    print("Invalid input format for inputs. Please enter comma-separated integers.")
                    continue

            # Filter out any characters that are not valid Brainfuck instructions
            valid_chars = "+-<>,.[]"
            program = "".join(c for c in program_input if c in valid_chars)

            if not program:
                print("No valid Brainfuck instructions found in the input. Please try again.")
                continue

            # Create an instance of the StateMachine
            sm = machine.StateMachine(program, inputs)
            
            print("\nRunning program...")
            # Run the program until it completes
            sm.run() 

            # Display the raw integer outputs
            print("\nOutputs (raw integer values):", sm.outputs)
            
            # Attempt to convert outputs to characters if they are within ASCII range
            try:
                char_outputs = "".join(chr(o) for o in sm.outputs if 0 <= o <= 255)
                if char_outputs:
                    print("Outputs (as characters):", char_outputs)
            except ValueError:
                print("Note: Some outputs are not valid ASCII character codes (0-255) and could not be converted to characters.")

        except IndexError as e:
            # Catch errors related to unmatched brackets or out-of-bounds access
            print(f"Error: {e}. This often indicates an unmatched bracket in your Brainfuck code.")
        except Exception as e:
            # Catch any other unexpected errors during execution
            print(f"An unexpected error occurred: {e}")
            print("Please check your Brainfuck code and inputs.")

if __name__ == "__main__":
    # Ensure the main function is called when the script is executed directly
    main()
