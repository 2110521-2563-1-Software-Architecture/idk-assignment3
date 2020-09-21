import wx


class BaseView(wx.Frame):

    def __init__(self, title):
        wx.Frame.__init__(self, None, wx.ID_ANY, title, size=(500, 400))

    def init_ui(self):
        pass

    def set_presenter(self, presenter):
        self.presenter = presenter
