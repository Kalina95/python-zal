from view.view_styles import ViewFrameStyle
from view.model.mkframe import MkFrame


class View(MkFrame):

    def __init__(self, parent):
        super().__init__(parent=parent, bg_color=ViewFrameStyle.background_color)

    def create_frame(self):
        super().pack(fill="both", expand=True)

    def destroy_frame(self):
        self.pack_forget()
        self.destroy()
