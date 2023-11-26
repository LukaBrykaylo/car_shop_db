from t08_flask_mysql.app.my_project.auth.service import chassis_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class ChassisController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = chassis_service
