from t08_flask_mysql.app.my_project.auth.service import test_drive_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class TestDriveController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = test_drive_service
