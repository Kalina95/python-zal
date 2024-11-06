from service.log.nbp_service import NbpService
from view.model.view import View
from view.model.mkbutton import MkButton
from view.model.mklabel import MkLabel
from view.widget.logger import Logger
from view.model.mkrow import MkRow


class NbpApiView(View):

    def __init__(self, parent):
        super().__init__(parent=parent.main_window)
        self.nbp_service = NbpService._nbp_service_instance
        self.logger = None

        self.__init_title()
        self.__init_logger()
        self.__init_logger_switch()
        self.create_frame()

    def __init_title(self):
        title_row = MkRow(self)
        top_label = MkLabel("NBP API", title_row)
        top_label.pack_center()
        title_row.pack()

    def __init_logger_switch(self):
        logger_switch_row = MkRow(self)
        logger_switch = MkButton("Start/Stop", self.__toggle_status, logger_switch_row)
        logger_switch.pack_left()
        logger_switch_row.pack()

    def __init_logger(self):
        logger_row = MkRow(self)
        logger = Logger(logger_row,  self.nbp_service)
        logger.pack_center()
        logger_row.pack()
        self.logger = logger

    def __toggle_status(self):
        if not self.nbp_service.is_running:
            self.nbp_service.start()
        else:
            self.nbp_service.stop()




