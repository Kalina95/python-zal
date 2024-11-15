import json
import os
from typing import Any

from service.repository.repository import Repository


class FileRepository(Repository):
    """
    A repository class for managing entries in a file-based storage system.

    This class provides methods to add, retrieve, delete, and list entries stored in a file.
    Each entry is represented as a JSON object, and all entries are stored line-by-line in the file.
    The `FileRepository` is initialized with a specific model class type to enforce type-checking
    when adding new entries.
    """

    def __init__(self, filepath: str, model_class: type) -> None:
        self.filepath = filepath
        self.model_class = model_class
        super().__init__()

    def get(self, uid: int) -> Any:
        entries = self.get_all()
        for entry in entries:
            if entry['uid'] == uid:
                return entry
        raise ValueError(f"No entry found with UID: {uid}")

    def post(self, entry: object) -> int:
        if not isinstance(entry, self.model_class):
            raise TypeError(f"Only {self.model_class.__name__} instances can be added.")

        with open(self.filepath, 'a') as file:
            entry.uid = self.get_last_uid() + 1
            file.write(json.dumps(entry.__dict__) + "\n")

        return entry.uid

    def delete(self, uid: int) -> None:
        entries = self.get_all()
        updated_entries = [entry for entry in entries if entry['uid'] != uid]

        with open(self.filepath, 'w') as file:
            for entry in updated_entries:
                file.write(json.dumps(entry) + "\n")

    def get_all(self) -> list[str]:
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as file:
                entries = [json.loads(line.strip()) for line in file.readlines()]
                return entries
        else:
            raise FileNotFoundError(f"The file '{self.filepath}' does not exist.")

    def get_last_uid(self) -> int:
        entries = self.get_all()
        if not entries:
            return 0
        last_uid = max(entry['uid'] for entry in entries)
        return int(last_uid)

