from .note import Note

class Notebook:
    def __init__(self):
        self.notes = []

    def add_note(self, title, content, tags=None):
        self.notes.append(Note(title, content, tags))
        return f"Note {title} added."

    def edit_note(self, title, new_content):
        for note in self.notes:
            if note.title == title:
                note.content = new_content
                return f"Note {title} updated."
        return f"Note {title} not found."
    
    def find_note(self, title):
        for note in self.notes:
            if note.title == title:
                return str(note)
        return f"Note '{title}' not found."
    
    def show_all_notes(self):
        if not self.notes:
            return "No notes available."
        return "\n".join(str(note) for note in self.notes)

    def delete_note(self, title):
        for note in self.notes:
            if note.title == title:
                self.notes.remove(note)
                return f"Note {title} deleted."
        return f"Note {title} not found."

    def add_tag(self, title, tag):
        for note in self.notes:
            if note.title == title:
                note.tags.append(tag)
                return f"Tag(s) added to {title}."
        return f"Note {title} not found."

    def search_by_tag(self, tag):
        tagged_notes = [note for note in self.notes if tag in note.tags]
        if not tagged_notes:
            return "No notes found with that tag."
        return "\n".join(str(note) for note in tagged_notes)


    