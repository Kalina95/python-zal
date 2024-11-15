from tkinter import Frame

from view.model.baseframe import BaseFrame
from view.view_styles import ViewFrameStyle


class ViewFrame(BaseFrame):

    """
    A Frame widget that automatically packs itself with a white background.

    This widget is used as a building block for creating rows in the UI,
    particularly in the NbpApiView for titles.
    """

    def __init__(self, parent: Frame) -> None:
        super().__init__(parent=parent, bg_color=ViewFrameStyle.background_color)

    def create_frame(self) -> None:
        super().pack(fill="both", expand=True)
