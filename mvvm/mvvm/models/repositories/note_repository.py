from typing import List
from mvvm.models.entities.note import Note


class NoteRepository:

    def __init__(self):
        self.notes = [
            Note("Sample Note 1"),
            Note("Sample Note 2")
        ]

    def add_note(self, content: str):
        note = Note(content)
        self.notes.append(note)

    def remove_note(self, note):
        note_index = self.notes.index(note)
        if note_index >= 0:
            self.notes = self.notes[:note_index] + self.notes[note_index + 1:]

    def get_all_notes(self) -> List[Note]:
        return self.notes[:]

    def clear_all_notes(self):
        self.notes = []
