from service.http.http_service import HttpService



class NbpDollarHttpService(HttpService):
    """
    Service for fetching USD exchange rates from NBP (National Bank of Poland) API.
    The service connects to the NBP API endpoint for USD exchange rates.
    Rate limits and API documentation: http://api.nbp.pl/
    """

    BASE_URL = "https://api.nbp.pl/api"
    ENDPOINT = "exchangerates/rates/a/usd"

    def __init__(self) -> None:
        super().__init__(self.BASE_URL, self.ENDPOINT)

    def get(self) -> str:
        return super().get()