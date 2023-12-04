from t08_flask_mysql.app.my_project.auth.dao import photo_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class PhotoService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = photo_dao

    def add_ten_photos(self):
        self._dao.add_ten_photos()