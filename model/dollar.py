from dataclasses import dataclass
from datetime import datetime


@dataclass
class Dollar:
    """
    Represents a dollar price record with unique identifier, date, and price.
    This class is used to store and manage gold price data fetched from NBP service.
    """
    uid: int
    date: str
    price: float

    def __post_init__(self) -> None:
        if self.price < 0:
            raise ValueError("Price cannot be negative")
        try:
            datetime.strptime(self.date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format")