from typing import List

import rx
from rx import operators as ops
from rx.subject import BehaviorSubject

from mvvm.models.entities.note import Note
from mvvm.models.repositories.note_repository import NoteRepository


class MainViewModel:

    def __init__(self):
        self.note_repository = NoteRepository()
        # Create notes field as a behavior subject with note from the business logic as an initial value
        # Your code here

    def add_note(self, note: str):
        # Add note and emit event with new date to the subject
        # Your code here
        pass

    def clear_all(self):
        # Clear all note and emit event with new data to the subject
        # Your code here
        pass
