
from service.chart.chart_component import ChartComponent
from view.model.viewframe import ViewFrame


class NbpResultsView(ViewFrame):
    def __init__(self, parent) -> None:
        super().__init__(parent=parent)
        self.parent = parent
        self.chart_component = ChartComponent(self)
