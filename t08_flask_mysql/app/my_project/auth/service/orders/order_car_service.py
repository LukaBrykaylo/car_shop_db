from t08_flask_mysql.app.my_project.auth.dao import order_car_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class OrderCarService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = order_car_dao

    def find_cars_by_order_id(self, order_id: int):
        return self._dao.find_cars_by_order_id(order_id)

    def find_orders_by_car_id(self, car_id: int):
        return self._dao.find_orders_by_car_id(car_id)
