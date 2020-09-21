import wx
from mvvm.views.main_view import MainView


class MvvmNoteApplication:

    def main(self):
        # Setup view
        app = wx.App()
        main_view = MainView()

        # Setup first page
        main_view.Show(True)

        # Start application
        app.MainLoop()


if __name__ == "__main__":
    application = MvvmNoteApplication()
    application.main()
