from service.log.nbp_log_service import NbpLogService
from view.view_manager import ViewManager

'''
This application is a financial data visualization tool that displays real-time Gold and Dollar prices
retrieved from the National Bank of Poland (NBP) API. The data is periodically updated and logged,
and users can view trends through an interactive PyQt5 interface.

It is written in Python using the PyQt5 library, making it a cross-platform GUI application that
integrates data retrieval, logging, and visualization components.
'''

# create initializer and assign main window
nbp_service = NbpLogService()
view_manager = ViewManager()
view_manager.start_application()
