from t08_flask_mysql.app.my_project.auth.dao import chassis_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class ChassisService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = chassis_dao

    def insert_into_chassis(self, chassis_model: str, chassis_wheel_number: int):
        self._dao.insert_into_chassis(chassis_model, chassis_wheel_number)
