import wx
from mvc.controllers.main_controller import MainController
from mvc.views.main_view import MainView


class MvcNoteApplication:

    def main(self):
        # Setup view
        app = wx.App()
        controller = MainController()
        main_view = MainView(controller)

        # Setup first page
        main_view.Show(True)

        # Start application
        app.MainLoop()


if __name__ == "__main__":
    application = MvcNoteApplication()
    application.main()
