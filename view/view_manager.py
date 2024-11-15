from view.model.viewframe import ViewFrame
from view.model.window import Window
from view.widget.menu import Menu

'''
MainWindow class contains main elements of GUI:
    - MenuFrame: Frames with buttons to switch between views.
    - ViewFrame: Frames to display content/data.
    - Window: The main window container for the application.
'''


class ViewManager:

    def __init__(self) -> None:
        self.main_window: Window = None
        self.menu_frame: Menu = None
        self.view_frame: ViewFrame = None

        self.__init_main_window()
        self.__init_menu_frame()

    def __init_main_window(self) -> None:
        self.tkWindow = Window("app title")

    def __init_menu_frame(self) -> None:
        self.menu_frame = Menu(self)

    def start_application(self) -> None:
        self.tkWindow.tk.mainloop()

    def update_view_frame(self, frame: ViewFrame) -> None:
        if self.view_frame is not None:
            self.view_frame.destroy_frame()
        self.view_frame = frame
        self.view_frame.create_frame()
        self.tkWindow.update()
