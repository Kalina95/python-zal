from abc import abstractmethod, ABC
from typing import Any, Optional


class Repository(ABC):
    """
    An abstract base class that defines a generic interface for data storage operations.

    This class provides a blueprint for implementing CRUD operations in derived classes.
    It includes methods for retrieving, posting, deleting, and listing data. Each method
    must be implemented in a subclass.
    """
    def __init__(self) -> None:
        self.storage_uri: Optional[str] = None

    @abstractmethod
    def get(self, key: int) -> Any:
        raise NotImplementedError

    @abstractmethod
    def post(self, value: Any) -> int:
        raise NotImplementedError

    @abstractmethod
    def delete(self, key: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> list[str]:
        raise NotImplementedError
