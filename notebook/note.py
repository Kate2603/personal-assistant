class Note:
    def __init__(self, title, content, tags: list):
        self.title = title
        self.content = content
        self.tags = tags

    def __repr__(self):
        return f"Title {self.title}\n Description {self.content}\nTags {', '.join(self.tags)} "