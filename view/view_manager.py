from service.chart.chart_service import ChartService
from view.widget.menu import Menu
from view.model.view import View
from view.model.window import Window

'''
MainWindow class cointains main elements of GUI:
    - MenuFrame - frames with buttons which determine what view to show. 
    - ViewFrame - frames which is used to show data.
    - Window - main window of application.
    
    Methods:
    - update_view_frame(frames: Frame) - updates view frames with new frames.
    
    Frames:
    - MenuFrame - frames
    - ViewFrame - frames
    - Window - frames
    - ViewFrame - frames '''


class ViewManager:

    def __init__(self):
        self.main_window: Window = None
        self.menu_frame: Menu = None
        self.view_frame: View = None

        self.__init_main_window()
        self.__init_menu_frame()

    def __init_main_window(self) -> None:
        self.tkWindow = Window("app title")

    def __init_menu_frame(self) -> None:
        self.menu_frame = Menu(self)

    def start_application(self) -> None:
        self.tkWindow.tk.mainloop()

    def update_view_frame(self, frame: View) -> None:
        if self.view_frame is not None:
            self.view_frame.destroy_frame()
        self.view_frame = frame
        self.view_frame.create_frame()
        self.tkWindow.update()
