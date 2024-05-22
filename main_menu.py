from prompt_toolkit import prompt
from prompt_tool import Completer, RainbowLexer

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    book = dict()
    print("Welcome to the assistant bot!")
    while True:
        user_input = prompt("Enter a command: ", completer=Completer, lexer=RainbowLexer)
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]: 
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            pass
        elif command == "change":
            pass
        elif command == "phone":
            pass
        elif command == "all":
            pass
        elif command == "add-birthday":
            pass
        elif command == "show-birthday":
            pass
        elif command == "birthdays":
            pass
        else:
            print("Invalid")

if __name__ == "__main__":
    main()