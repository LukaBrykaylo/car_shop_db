from t08_flask_mysql.app.my_project.auth.service import photo_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class PhotoController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = photo_service

    def add_ten_photos(self):
        self._service.add_ten_photos()
