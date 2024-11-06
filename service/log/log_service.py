import threading


class LogService:
    def __init__(self):
        self.records = []
        self.is_running: bool = False
        self.thread = None
        self.new_record = threading.Event()

    def _init_thread(self, function):
        self.thread = threading.Thread(target=function, daemon=True)
        self.thread.start()

    def __thread_main(self):
        pass

    def get_records(self):
        return self.records

    def get_last_record(self):
        if len(self.records) > 0:
            return self.records[-1]

    def set_new_record_event(self):
        self.new_record = threading.Event()

    def start(self):
        self.is_running = True

    def stop(self):
        self.is_running = False