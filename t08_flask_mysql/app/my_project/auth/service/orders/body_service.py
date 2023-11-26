from t08_flask_mysql.app.my_project.auth.dao import body_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class BodyService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = body_dao
