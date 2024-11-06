from datetime import datetime
from time import sleep

from model.dollar import Dollar
from model.gold import Gold
from service.http.http_dollar_http_service import NbpDollarHttpService
from service.http.http_service import HttpService
from service.http.nbp_gold_http_service import NbpGoldHttpService
from service.log.log_service import LogService
from service.repository.dollar_file_repository import DollarFileRepository
from service.repository.gold_file_repository import GoldFileRepository
from service.repository.repository import Repository


class NbpService(LogService):
    _nbp_service_instance = None
    _now = datetime.now()

    def __new__(cls, *args, **kwargs):
        if cls._nbp_service_instance is None:
            cls._nbp_service_instance = super(NbpService, cls).__new__(cls)
        return cls._nbp_service_instance

    def  __init__(self):
        self.gold_service: HttpService = NbpGoldHttpService()
        self.dollar_service: HttpService = NbpDollarHttpService()
        self.gold_repository: Repository = GoldFileRepository()
        self.dollar_repository: Repository = DollarFileRepository()

        super().__init__()
        self._init_thread(self.__thread_main)

    def __thread_main(self):
        while True:
            while self.is_running:
                gold_response = self.gold_service.get()
                dollar_response = self.dollar_service.get()
                self.__handle_response(gold_response, dollar_response)
                sleep(5)

    def __prepare_log(self, gold_price: str, dollar_price: str) -> str:
        log: str = f"[{self.__class__.__name__}] {self._now.strftime('%Y-%m-%d %H:%M:%S')} : gold price = {gold_price}, dollar price = {dollar_price}"
        print(log)
        return log

    def __handle_response(self, gold_response, dollar_response):
        parsed_gold_price = self.__parse_gold_price_response(gold_response)
        parsed_dollar_price = self.__parse_dollar_price_response(dollar_response)
        json = self.__prepare_log(parsed_gold_price, parsed_dollar_price)
        self.records.append(json)
        self.__save_data(parsed_gold_price, parsed_dollar_price)
        self.new_record.set()
        self.set_new_record_event()

    def __save_data(self, gold_price, dollar_price):
        date = self._now.strftime('%Y-%m-%d %H:%M:%S')
        self.dollar_repository.post(Dollar(0, date, dollar_price))
        self.gold_repository.post(Gold(0, date, gold_price))

    def __parse_gold_price_response(self, response):
        return response[0].get("cena")

    def __parse_dollar_price_response(self, response):
        return response.get("rates")[0].get("mid")