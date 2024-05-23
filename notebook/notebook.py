from .note import Note

class Notebook:
    def __init__(self):
        self.notes = []

    def add_note(self, title, content):
        self.notes.append(Note(title, content))
        return f"Note {title} added."

    def find_note_by_title(self, title):
        for note in self.notes:
            if note.title == title:
                return str(note)
        return f"Note {title} not found."

    def edit_note(self, title, new_content):
        for note in self.notes:
            if note.title == title:
                note.content = new_content
                return f"Note {title} updated."
        return f"Note {title} not found."

    def delete_note(self, title):
        for note in self.notes:
            if note.title == title:
                self.notes.remove(note)
                return f"Note {title} deleted."
        return f"Note {title} not found."

    