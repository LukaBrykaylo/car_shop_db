from t08_flask_mysql.app.my_project.auth.dao import drive_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class DriveService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = drive_dao
