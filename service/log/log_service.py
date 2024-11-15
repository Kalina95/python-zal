import threading
from abc import abstractmethod
from typing import Optional


class LogService:
    """
    A base class for services that require logging functionality and threading.

    This class provides logging capabilities, thread management, and event signaling for derived classes.
    Subclasses must implement the `__thread_main` method to define specific functionality for the thread.
    """
    def __init__(self) -> None:
        self.records = []
        self.is_running: bool = False
        self.thread: Optional[threading.Thread] = None
        self.new_record = threading.Event()

    def _init_thread(self, function) -> None:
        self.thread = threading.Thread(target=function, daemon=True)
        self.thread.start()

    @abstractmethod
    def __thread_main(self) -> None:
        pass

    def get_records(self) -> []:
        return self.records

    def get_last_record(self):
        if len(self.records) > 0:
            return self.records[-1]

    def set_new_record_event(self):
        self.new_record = threading.Event()

    def start(self) -> None:
        self.is_running = True

    def stop(self) -> None:
        self.is_running = False
