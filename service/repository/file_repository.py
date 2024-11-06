import json
import os
from service.repository.repository import Repository


class FileRepository(Repository):
    def __init__(self):
        self.filepath = None
        self.model_class = None
        super().__init__()

    def get(self, uid):
        entries = self.get_all()
        for entry in entries:
            if entry['uid'] == uid:
                return entry
        raise ValueError(f"No entry found with UID: {uid}")

    def post(self, entry):
        if not isinstance(entry, self.model_class):
            raise TypeError(f"Only {self.model_class.__name__} instances can be added.")

        with open(self.filepath, 'a') as file:
            entry.uid = self.get_last_uid() + 1
            file.write(json.dumps(entry.__dict__) + "\n")

    def delete(self, uid):
        entries = self.get_all()
        updated_entries = [entry for entry in entries if entry['uid'] != uid]

        with open(self.filepath, 'w') as file:
            for entry in updated_entries:
                file.write(json.dumps(entry) + "\n")

    def get_all(self):
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

