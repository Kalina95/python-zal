from service.http.http_service import HttpService


class NbpGoldHttpService(HttpService):
    """
    Service for fetching Gold exchange rates from NBP (National Bank of Poland) API.
    The service connects to the NBP API endpoint for Gold exchange rates.
    Rate limits and API documentation: http://api.nbp.pl/
    """

    BASE_URL = "https://api.nbp.pl/api"
    ENDPOINT = "cenyzlota"

    def __init__(self) -> None:
        super().__init__(self.BASE_URL, self.ENDPOINT)

    def get(self) -> str:
        return super().get()
