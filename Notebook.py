from datetime import datetime


class Note:
    """Note"""

    def __init__(self, memo, tags, notes=[]):
        """Constructor

        Args:
            memo (str): Your memo
            tags (str): tags for memo
            notes (list, optional): list of exist notes. Defaults to [].
        """
        self.memo = memo
        self.creation_time = datetime.now()
        self.creation_date = datetime.now().date()
        self.tags = tags
        self.id = len(notes)+1

    def __str__(self):
        """String for object

        Returns:
            str: info about note
        >>> note=Note("my name is Yurii", "Info about me")
        >>> print(str(note)[:-29]+'<time>')
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        Note ID:
        1
        <BLANKLINE>
        Your note:
        my name is Yurii
        <BLANKLINE>
        Tags for note:
        Info about me
        <BLANKLINE>
        Creation time:
        <time>
        """
        # <time> is different, so doctest was changed
        return f'\n\n\nNote ID:\n{self.id}\n\nYour note:\n{self.memo}\n\nTags for note:\n\
{self.tags}\n\nCreation time:\n{self.creation_time}\n\n\n'


class Notebook:
    """Notebook"""

    def __init__(self):
        """Constructor
        """
        self.notes = []

    def __str__(self):
        """returns info about notes
        """
        plural = 'note' if len(self.notes) == 1 else 'notes'
        return f'You have {len(self.notes)} {plural} in your notebook.'

    def new_note(self, memo, tags=''):
        """Adds new note to the notebook

        Args:
            memo (str): Your memo
            tags (str, optional): tags for memo. Defaults to ''.
        >>> note = Note("my name is Yurii", "Info about me")
        >>> notebook = Notebook()
        >>> notebook.new_note(note)
        >>> print(notebook)
        You have 1 note in your notebook.
        """
        self.notes.append((Note(memo, tags, self.notes)))

    def search(self, filter: str):
        """Search in notes

        Args:
            filter (str): regular expression which you're looking for

        Returns:
            list: found Notes
        """
        found = []
        for i in self.notes:
            if filter in i.memo or filter in i.tags:
                found.append(i)
        return found

    def modify_memo(self, note_id, memo):
        """Changes exist note

        Args:
            note_id (str): Note id
            memo (str): New text
        """
        self.notes[int(note_id)-1].memo = memo

    def modify_tags(self, note_id, tags):
        """Modifies tags for note

        Args:
            note_id (str): note id
            tags (str): new tags
        """
        self.notes[int(note_id)-1].tags = tags

    def note_by_id(self, note_id):
        """print information about note by its id

        Args:
            note_id (str): note id
        """
        print(self.notes[int(note_id)-1])
