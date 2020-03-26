import datetime

last_id = 1


class Note:
    """ Represent a note in the notebook"""

    def __init__(self, memo, tags=''):
        """initialize a note with memo and optional
        space-separated tags."""
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def modify(self, new_memo, new_tags):
        """ (Note, str) -> None
        Modifies an Note"""
        self.memo, self.tags = new_memo, new_tags

    def match(self, filter):
        """Determine if this note matches the filter
        text. Return True if it matches, False otherwise.
        Search is case sensitive and matches both text and tags."""
        return filter in self.memo or  filter in self.tags

    def __str__(self):
        """ Prints an object"""
        return '\n'.join([f"{self.memo}. TAGS: {self.tags}"
                          f"          CREATION DATE: {self.creation_date}"])


class Notebook:
    """Represent a collection of notes that can be tagged and searched"""

    def __init__(self):
        self.notes = []

    def new_note(self, memo, tags='None'):
        """ Adds a new note"""
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id, memo):
        """Find the note with the given id and change its
        memo to the given value."""
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False

    def _find_note(self, note_id):
        """Locate the note with the given id."""
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None

    def modify_tags(self, note_id, tags):
        """
        Find the note with the given id and change its tags to the given value.
        """
        for note in self.notes:
            if note.id == note_id:
                note.tags = tags
                break

    def search(self, filter):
        """Find all notes that match the given filter string."""
        return [note for note in self.notes if
                note.match(filter)]

    def delete_note(self, note_id):
        if self._find_note(id):
            self.notes.remove(id)
