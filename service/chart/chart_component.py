import threading

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from service.chart.chart_service import ChartService


class ChartComponent:
    def __init__(self, parent):
        self.parent = parent
        self.fig = Figure(figsize=(15, 15), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=parent)
        self.chart_service = ChartService(self.fig, self.canvas)
        self.chart_service.plot_data(self.fig)

        self.thread = threading.Thread(target=self.draw_canvas)
        self.thread.start()

    def draw_canvas(self):
        self.canvas.draw()

    def pack_canvas(self):
        self.canvas.get_tk_widget().pack(expand=False)
