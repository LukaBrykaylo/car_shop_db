from t08_flask_mysql.app.my_project.auth.service import car_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class CarController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = car_service

    def find_orders(self, car_id: int):
        return self._service.find_orders(car_id)
