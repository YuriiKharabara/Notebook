from Notebook import *
import sys

class Menu:
    def __init__(self):
        self.notebook=Notebook()
        self.choices={
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.show_note,
            "6": self.quit
        }
    def display_menu(self):
        """Display menu on the screen.
        """
        print("""
            Notebook Menu
            1. Show all Notes
            2. Search Notes
            3. Add Note
            4. Modify Note
            5. Show note by id
            6. Quit
        """)
    def run(self):
        """Start executing the program, take user choices.
        """
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))
    
    def show_notes(self, notes: Note = None):
        """Show notes contents.

        Args:
            notes (Note, optional): Note to show conctents. Defaults to None.
        """
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{0}: {1}\n{2}\n\t\tCreation date: {3}".format(note.id, note.tags, note.memo, note.creation_date))

    def show_note(self):
        note_id=input("Enter id: ")
        self.notebook.note_by_id(note_id)
    def search_notes(self):
        """Searches notes in the notebook and show them.
        """
        filterr = input("Search for: ")
        notes = self.notebook.search(filterr)
        self.show_notes(notes)

    def add_note(self):
        """Add a new note to the notebook.
        """
        memo = input("Enter a memo: ")
        tags = input("Enter tags(or enter): ")
        self.notebook.new_note(memo, tags)
        print("Your note has been added.")

    def modify_note(self):
        """Change memo or tags of the note.
        """
        id = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        """Stop the program.
        """
        print("Thank you for using your notebook today.")
        sys.exit(0)

if __name__=='__main__':
    Menu().run()