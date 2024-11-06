from matplotlib.figure import Figure

import utils.utils as utils
from service.repository.dollar_file_repository import DollarFileRepository
from service.repository.gold_file_repository import GoldFileRepository
from service.repository.repository import Repository


class ChartService:
    def __init__(self, figure, canvas):

        self.temp_fig: figure
        self.temp_canvas = canvas

        self.tk_parent = None
        self.gold_data = None
        self.dollar_data = None

        self.gold_repository: Repository = GoldFileRepository()
        self.dollar_repository: Repository = DollarFileRepository()

        self.__load_data()

    def plot_data(self, fig: Figure):
        ax1 = fig.add_subplot(211)

        if self.gold_data is not None:
            ax1.plot(self.gold_data['date'], self.gold_data['price'], label="Gold Price", color="gold", marker="o")

        if self.dollar_data is not None:
            ax1.plot(self.dollar_data['date'], self.dollar_data['price'] * 100, label="Dollar Price", color="green",
                     marker="o")

        ax1.set_xlabel("Date")
        ax1.set_ylabel("Price")
        if self.dollar_data is not None:
            ax1.set_title("Dollar Prices")
        elif self.dollar_data is not None:
            ax1.set_title("Gold Prices")
        else:
            ax1.set_title("Gold and Dollar Prices")
        ax1.legend()

    def __load_data(self):
        self.__load_gold_data()
        self.__load_dollar_data()

    def __load_gold_data(self):
        self.gold_data = utils.parse(self.gold_repository.get_all())
        print(utils.parse(self.gold_repository.get_all()))

    def __load_dollar_data(self):
        self.dollar_data = utils.parse(self.dollar_repository.get_all())
        print(utils.parse(self.dollar_repository.get_all()))