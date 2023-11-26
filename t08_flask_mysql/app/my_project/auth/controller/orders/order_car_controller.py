from t08_flask_mysql.app.my_project.auth.service import order_car_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class OrderCarController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = order_car_service

    def find_cars_by_order_id(self, order_id: int):
        return self._service.find_cars_by_order_id(order_id)

    def find_orders_by_car_id(self, car_id: int):
        return self._service.find_orders_by_car_id(car_id)