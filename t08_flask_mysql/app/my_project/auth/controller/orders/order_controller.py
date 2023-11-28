from t08_flask_mysql.app.my_project.auth.service import order_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class OrderController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = order_service

    def find_cars(self, order_id: int):
        return self._service.find_cars(order_id)