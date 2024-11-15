from model.dollar import Dollar
from service.repository.file_repository import FileRepository


class DollarFileRepository(FileRepository):
    """Repository for managing dollar data persistence in a file."""

    DEFAULT_FILE_PATH = "./resources/database_dollar.txt"

    def __init__(self, filepath: str = None):
        self.filepath = filepath or self.DEFAULT_FILE_PATH
        self.model_class = Dollar
        super().__init__(self.filepath, self.model_class)
