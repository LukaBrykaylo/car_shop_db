from t08_flask_mysql.app.my_project.auth.dao import test_drive_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class TestDriveService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = test_drive_dao
