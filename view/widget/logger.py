import threading
import tkinter as tk

from service.log.log_service import LogService
from view.model.baseframe import BaseFrame
from view.model.label import Label
from view.model.row import Row
from view.model.textarea import TextArea


class Logger(BaseFrame):

    def __init__(self, parent: tk.Frame, service: LogService) -> None:
        super().__init__(parent=parent, bg_color="white")
        self.service = service

        self.componentAlive = True
        self.logs_area_row = Row(self)
        self.logs_area = TextArea(self.logs_area_row)
        self.logs_area.pack_center()
        self.status_label = Label("Status: Off", self)
        self.__print_previous_logs()

        self.logger_thread = threading.Thread(target=self.__printing_logs)
        self.logger_thread.start()

    def __init_label(self) -> None:
        self.label_row = Row(self)
        self.log_label = Label("Logi zbierane z NbpAPi: ceny złota w danym dniu", self.label_row)
        self.log_label.pack_left()

    def append_log(self, message: str) -> None:
        if self.componentAlive:
            self.logs_area.config(state="normal")
            self.logs_area.insert(tk.END, message + "\n")
            self.logs_area.see(tk.END)
            self.logs_area.config(state="disabled")

    def refresh_logs_area(self) -> None:
        self.logs_area.destroy_area()
        self.logs_area = TextArea(self.logs_area_row)
        self.logs_area.pack_center()

    def __change_status_label(self) -> None:
        if self.service.is_running:
            self.status_label.config(text="Status: Running", fg="green")
        else:
            self.status_label.config(text="Status: Stopped", fg="red")

    def __print_previous_logs(self) -> None:
        for record in self.service.get_records():
            self.append_log(record)

    def __printing_logs(self) -> None:
        while self.componentAlive:
            if self.service.is_running:
                self.service.new_record.wait()
                log = self.service.get_last_record()
                if log:
                    self.append_log(log)

    def destroy(self) -> None:
        self.componentAlive = False
        self.logger_thread.join(timeout=0.1)
        super().destroy()
