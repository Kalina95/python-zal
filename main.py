from service.log.nbp_service import NbpService
from view.view_manager import ViewManager

'''
This application is a ...
It is written in Python using the PyQt5 library.
'''

# create initializer and assign main window
nbp_service = NbpService()
view_manager = ViewManager()
view_manager.start_application()
