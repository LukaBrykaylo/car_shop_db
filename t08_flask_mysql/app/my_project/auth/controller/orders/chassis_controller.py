from t08_flask_mysql.app.my_project.auth.service import chassis_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class ChassisController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = chassis_service

    def insert_into_chassis(self, chassis_model: str, chassis_wheel_number: int):
        self._service.insert_into_chassis(chassis_model, chassis_wheel_number)
