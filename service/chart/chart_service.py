import logging

from matplotlib.axes import Axes
from matplotlib.figure import Figure

import utils.utils as utils
from service.repository.dollar_file_repository import DollarFileRepository
from service.repository.gold_file_repository import GoldFileRepository
from service.repository.repository import Repository


class ChartService:
    """
     A service class to load, manage, and visualize Gold and Dollar price data.

    This class interfaces with repositories to fetch data for Gold and Dollar prices,
    processes the data, and provides methods to plot it using Matplotlib.
    """
    def __init__(self) -> None:
        self.gold_data = None
        self.dollar_data = None

        self.gold_repository: Repository = GoldFileRepository()
        self.dollar_repository: Repository = DollarFileRepository()

        self.__load_data()

    def plot_data(self, fig: Figure) -> None:
        ax = fig.add_subplot(211)
        self.__plot_gold_data(ax)
        self.__plot_dollar_data(ax)
        self.__plot_legend(ax)

    def __plot_legend(self, ax: Axes) -> None:
        ax.set_xlabel("Date")
        ax.set_ylabel("Price")
        if not self.__is_dollar_data_empty() and not self.__is_gold_data_empty():
            ax.set_title("Gold and Dollar Prices")
        elif not self.__is_gold_data_empty():
            ax.set_title("Gold Prices")
        else:
            ax.set_title("Dollar Prices")
        ax.legend()

    def __plot_gold_data(self, ax: Axes) -> None:
        if not self.__is_gold_data_empty():
            ax.plot(self.gold_data['date'], self.gold_data['price'], label="Gold Price", color="gold", marker="o")

    def __plot_dollar_data(self, ax: Axes) -> None:
        # Multiply dollar price by 100 for better visualization on the same scale as gold
        if not self.__is_dollar_data_empty():
            ax.plot(self.dollar_data['date'], self.dollar_data['price'] * 100, label="Dollar Price", color="green",
                    marker="o")

    def __is_dollar_data_empty(self) -> bool:
        return self.dollar_data is None or self.dollar_data.empty

    def __is_gold_data_empty(self) -> bool:
        return self.gold_data is None or self.gold_data.empty

    def __load_data(self) -> None:
        self.__load_gold_data()
        self.__load_dollar_data()

    def __load_gold_data(self) -> None:
        try:
            self.gold_data = utils.parse(self.gold_repository.get_all())
        except Exception as e:
            logging.error(f"Error loading gold data: {e}")

    def __load_dollar_data(self) -> None:
        try:
            self.dollar_data = utils.parse(self.dollar_repository.get_all())
        except Exception as e:
            logging.error(f"Error loading dollar data: {e}")
