from t08_flask_mysql.app.my_project.auth.service import drive_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class DriveController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = drive_service
