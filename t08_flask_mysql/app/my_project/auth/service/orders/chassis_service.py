from t08_flask_mysql.app.my_project.auth.dao import chassis_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class ChassisService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = chassis_dao
