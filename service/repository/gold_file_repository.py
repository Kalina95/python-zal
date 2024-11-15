from model.gold import Gold
from service.repository.file_repository import FileRepository


class GoldFileRepository(FileRepository):
    """Repository for managing gold data persistence in a file."""

    DEFAULT_FILE_PATH = "./resources/database_gold.txt"

    def __init__(self, filepath:str = None):
        self.filepath = filepath or self.DEFAULT_FILE_PATH
        self.model_class = Gold
        super().__init__(self.filepath, self.model_class)
