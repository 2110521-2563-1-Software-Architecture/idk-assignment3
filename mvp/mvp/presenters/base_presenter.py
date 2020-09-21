from mvp.views.base_view import BaseView


class BasePresenter:

    def __init__(self, view: BaseView):
        self.view = view
        self.view.set_presenter(self)
