from mvc.models.repositories.note_repository import NoteRepository

class MainController(NoteRepository):
    def __init__(self):
        super().__init__()
        pass
    
    def get_all_notes(self):
        return NoteRepository.get_all_notes(self)
        pass

    def add_note(self, note: str):
        NoteRepository.add_note(self,note)
        pass

    def clear_all(self):
        NoteRepository.clear_all_notes(self)
        pass
