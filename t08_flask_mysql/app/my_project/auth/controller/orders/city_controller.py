from t08_flask_mysql.app.my_project.auth.service import city_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class CityController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = city_service

    def find_shops_by_index(self, city_id: int):
        return self._service.find_shops_by_index(city_id)
