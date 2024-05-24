from .note import Note

class Notebook:
    def __init__(self):
        self.notes = []

    def add_note(self, title, content, tags):
        self.notes.append(Note(title, content, tags))
        return f"Note {title} added."

    def find_note_by_title(self, title):
        for note in self.notes:
            if note.title == title:
                return str(note)
        return f"Note {title} not found."
    
    def find_note_by_tag(self, tag):
        search_result = []
        for note in self.notes:
            if tag in note.tags: 
                search_result.append(note)
        if len(search_result)<1:
            return f"Note with {tag} not found."
        else:
            return search_result

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
    
    def sort_notes_by_tags(self, reverse=False, alphabet_mode=True):
        def sort_algorithm(x):
            tags = x.tags
            print(tags,len(tags))
            if alphabet_mode is True and tags:
                return ord(x.tags[0][0])
            else:
                return 123
        self.notes.sort(key=sort_algorithm,reverse=reverse)
        return self.notes
    
    def __repr__(self) -> str:
        return "\n".join(self.notes)


    