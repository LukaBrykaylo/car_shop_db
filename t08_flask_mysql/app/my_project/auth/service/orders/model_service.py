from t08_flask_mysql.app.my_project.auth.dao import model_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class ModelService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = model_dao
