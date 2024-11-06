from service.http.http_service import HttpService


class NbpGoldHttpService(HttpService):
    def __init__(self):
        super().__init__()
        self.base_url = "https://api.nbp.pl/api"
        self.endpoint = "cenyzlota"

    def get(self) -> str:
        return super().get()
