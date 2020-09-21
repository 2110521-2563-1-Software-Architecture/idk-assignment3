import wx
from mvp.views.main_view import MainView
from mvp.presenters.main_presenter import MainPresenter
from mvp.models.repositories.note_repository import NoteRepository


class MvpNoteApplication:

    def main(self):
        # Setup dependencies
        note_repository = NoteRepository()

        # Setup view
        app = wx.App()
        main_view = MainView()

        # Setup presenter
        main_presenter = MainPresenter(main_view, note_repository)

        # Setup first page
        main_view.init_ui()
        main_view.Show(True)

        # Start application
        app.MainLoop()


if __name__ == "__main__":
    application = MvpNoteApplication()
    application.main()
