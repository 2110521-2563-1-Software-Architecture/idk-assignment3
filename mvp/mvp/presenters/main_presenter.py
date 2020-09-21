from typing import List
from mvp.contracts.main_contract import MainContract
from mvp.models.repositories.note_repository import NoteRepository
from mvp.models.entities.note import Note


class MainPresenter(MainContract.Presenter):

    def __init__(self, view: MainContract.View, note_repository: NoteRepository):
        MainContract.Presenter.__init__(self, view)
        self.note_repository = note_repository

    # Your code here
