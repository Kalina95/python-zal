import threading
import tkinter as tk

from service.log.log_service import LogService
from view.model.mkframe import MkFrame
from view.model.mklabel import MkLabel
from view.model.mkrow import MkRow
from view.model.mkscrolledtext import MkScrolledText


class Logger(MkFrame):

    def __init__(self, parent, service: LogService):
        super().__init__(parent=parent, bg_color="white")
        self.service = service

        self.componentAlive = True
        self.logs_area_row = MkRow(self)
        self.logs_area = MkScrolledText(self.logs_area_row)
        self.logs_area.pack_center()
        self.status_label = MkLabel("Status: Off", self)
        self.__print_previous_logs()

        # thread and injection
        self.logger_thread = threading.Thread(target=self.__printing_logs)
        self.logger_thread.start()

    def __init_label(self):
        self.label_row = MkRow(self)
        self.log_label = MkLabel("Logi zbierane z NbpAPi: ceny złota w danym dniu", self.label_row)
        self.log_label.pack_left()

    def append_log(self, message):
        if self.componentAlive:
            self.logs_area.config(state="normal")
            self.logs_area.insert(tk.END, str(message) + "\n")
            self.logs_area.see(tk.END)
            self.logs_area.config(state="disabled")

    def refresh_logs_area(self):
        self.logs_area.destroy_area()
        self.logs_area = MkScrolledText(self.logs_area_row)
        self.logs_area.pack_center()

    def __change_status_label(self):
        if self.service.is_running:
            self.status_label.config(text="Status: Running", fg="green")
        else:
            self.status_label.config(text="Status: Stopped", fg="red")

    def __print_previous_logs(self):
        for record in self.service.get_records():
            self.append_log(record)

    def __printing_logs(self):
        while self.componentAlive:
            if self.service.is_running:
                self.service.new_record.wait()
                log = self.service.get_last_record()
                if log:
                    self.append_log(log)

    def destroy(self):
        self.componentAlive = False
        self.logger_thread.join(timeout=0.1)
        super().destroy()
