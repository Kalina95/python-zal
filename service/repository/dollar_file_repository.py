from service.repository.file_repository import FileRepository


class DollarFileRepository(FileRepository):
    def __init__(self):
        self.filepath = "./resources/database_dollar.txt"
        super().__init__()
