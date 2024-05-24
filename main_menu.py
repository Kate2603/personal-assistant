from prompt_toolkit import prompt
from prompt_tool import Completer, RainbowLexer
from notebook.notebook import Notebook


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Give me name."
        except KeyError:
            return "Contact not found."

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_note(book: Notebook):
    title = input("enter the title: ")
    content = input("enter content: ")
    tags = input("enter tags separate by comas: ")
    tags = [tag.strip() for tag in tags.split(",") if tag != '']
    return book.add_note(title, content, tags)
    
@input_error
def find_note_by_tag(args, book:Notebook):
    tag = args[0]
    return book.find_note_by_tag(tag)

@input_error
def sort_notes(args, book:Notebook):
    return book.sort_notes_by_tags()


def main():
    book = Notebook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = prompt("Enter a command: ", completer=Completer, lexer=RainbowLexer())
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
        elif command == "add-note":
            print(add_note(book))
        elif command == "find-tag":
            print(find_note_by_tag(args, book))
        elif command == "sort-notes":
            print (sort_notes(args, book))
        else:
            print("Invalid")

if __name__ == "__main__":
    main()