from model.gold import Gold
from service.repository.file_repository import FileRepository


class GoldFileRepository(FileRepository):
    def __init__(self):
        self.filepath = "./resources/database_gold.txt"
        self.model_class = Gold
        super().__init__()
