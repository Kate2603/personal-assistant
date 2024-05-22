import pickle
import os
from collections import UserDict

# Note classes
class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def edit(self, new_content):
        self.content = new_content

    def __str__(self):
        return f"Title: {self.title}, Content: {self.content}"


class NoteBook(UserDict):
    def add_note(self, note):
        self.data[note.title] = note

    def find(self, title):
        return self.data.get(title)

    def delete(self, title):
        if title in self.data:
            del self.data[title]


# Command handling functions
def parse_input(user_input):
    return user_input.split(maxsplit=2)


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return str(e)
    return wrapper

# Note handling functions
@input_error
def add_note(args, notebook):
    title, content = args
    note = Note(title, content)
    notebook.add_note(note)
    return f"Note '{title}' added."


@input_error
def find_note(args, notebook):
    title, *_ = args
    note = notebook.find(title)
    if note:
        return str(note)
    else:
        return f"Note '{title}' not found."


@input_error
def edit_note(args, notebook):
    title, new_content = args
    note = notebook.find(title)
    if note:
        note.edit(new_content)
        return f"Note '{title}' updated."
    else:
        return f"Note '{title}' not found."


@input_error
def delete_note(args, notebook):
    title, *_ = args
    notebook.delete(title)
    return f"Note '{title}' deleted."