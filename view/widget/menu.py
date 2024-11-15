from view.widget.nbp_api_view_frame import NbpApiView
from view.model.button import Button
from view.model.baseframe import BaseFrame
from view.view_styles import MenuStyle
from view.widget.nbp_results_view_frame import NbpResultsView


class Menu(BaseFrame):

    def __init__(self, view_manager):
        super().__init__(parent=view_manager.main_window, bg_color=MenuStyle.background_color)
        self.view_manager = view_manager
        self.__init_buttons()
        self.create_frame()


    def __init_buttons(self) -> None :
        self.nbp_api_button = Button("NBP API", self.show_nbp_api, self)
        self.nbp_results_button = Button("NBP Results", self.show_nbp_results, self)
        self.nbp_api_button.pack_center()
        self.nbp_results_button.pack_center()

    def create_frame(self) -> None :
        super().pack(side="left", fill="both", expand=False)

    def show_nbp_api(self) -> None :
        self.view_manager.update_view_frame(NbpApiView(self.view_manager.main_window))

    def show_nbp_results(self) -> None :
        self.view_manager.update_view_frame(NbpResultsView(self.view_manager.main_window))
