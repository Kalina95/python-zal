
from service.chart.chart_component import ChartComponent
from view.model.viewframe import ViewFrame


class NbpResultsView(ViewFrame):
    def __init__(self, parent) -> None:
        super().__init__(parent=parent.main_window)
        self.parent = parent.main_window
        self.chart_component = ChartComponent(self.parent)
