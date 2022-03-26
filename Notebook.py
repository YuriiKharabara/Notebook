from datetime import datetime


class Note:
    def __init__(self, memo, tags, notes=[]):
        self.memo = memo
        self.creation_time = datetime.now()
        self.creation_date = datetime.now().date()
        self.tags = tags
        self.id = len(notes)+1

    def __str__(self):
        return f'\n\n\nNote ID:\n{self.id}\n\nYour note:\n{self.memo}\n\nTags for note:\n\
{self.tags}\n\nCreation time:\n{self.creation_time}\n\n\n'


class Notebook:
    def __init__(self):
        self.notes = []

    def new_note(self, memo, tags=''):
        self.notes.append((Note(memo, tags, self.notes)))

    def search(self, filter: str):
        found = []
        for i in self.notes:
            if filter in i.memo or filter in i.tags:
                found.append(i)
        return found

    def modify_memo(self, note_id, memo):
        self.notes[int(note_id)-1].memo = memo

    def modify_tags(self, note_id, tags):
        self.notes[int(note_id)-1].tags = tags
    
    def note_by_id(self, note_id):
        print(self.notes[int(note_id)-1])
