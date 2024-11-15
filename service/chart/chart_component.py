import threading

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from service.chart.chart_service import ChartService
from view.model.viewframe import ViewFrame


class ChartComponent:
    """
    Manages chart rendering and display in a Tkinter application.

    This component handles the creation, drawing, and display of matplotlib
    charts within a Tkinter parent widget using a separate thread for rendering.
    """
    def __init__(self, parent) -> None:
        self.parent: ViewFrame = parent
        self.fig = Figure(figsize=(15, 15), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=parent)
        self.chart_service = ChartService()
        self.chart_service.plot_data(self.fig)

        self.thread = threading.Thread(target=self.draw_canvas)
        self.thread.start()

    def draw_canvas(self) -> None:
        self.canvas.draw()
        self.pack_canvas()

    def pack_canvas(self) -> None:
        self.canvas.get_tk_widget().pack(expand=False)
