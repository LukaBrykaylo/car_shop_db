from t08_flask_mysql.app.my_project.auth.dao import engine_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class EngineService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = engine_dao
