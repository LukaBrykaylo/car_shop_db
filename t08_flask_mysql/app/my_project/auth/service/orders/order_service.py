from t08_flask_mysql.app.my_project.auth.dao import order_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class OrderService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = order_dao

    def find_cars(self, order_id: int):
        return self._dao.find_cars(order_id)

    def add_car_to_order(self, order_id: int, car_id: int):
        self._dao.add_car_to_order(order_id, car_id)

    def remove_car_from_order_id(self, order_id: int, car_id: int):
        self._dao.remove_car_from_order_id(order_id, car_id)
