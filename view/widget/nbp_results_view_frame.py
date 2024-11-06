from service.chart.chart_component import ChartComponent
from view.model.view import View


class NbpResultsView(View):
    def __init__(self, parent):
        super().__init__(parent=parent.main_window)
        self.parent = parent.main_window
        self.chart_component = ChartComponent(self.parent)
        self.chart_component.draw_canvas()
        self.chart_component.pack_canvas()
