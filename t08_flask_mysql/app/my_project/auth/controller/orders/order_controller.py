from t08_flask_mysql.app.my_project.auth.service import order_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class OrderController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = order_service

    def find_cars(self, order_id: int):
        return self._service.find_cars(order_id)

    def add_car_to_order(self, order_id: int, car_id: int):
        self._service.add_car_to_order(order_id, car_id)

    def remove_car_from_order_id(self, order_id: int, car_id: int):
        self._service.remove_car_from_order_id(order_id, car_id)
