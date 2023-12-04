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

    def insert_into_order_car_with_checks(self, order_id: int, car_length:int, car_width: int, car_engine_id: int,
                                          car_body_id: int, car_body_type: str, car_chassis_id: int, car_drive_id: int,
                                          car_photo_id: int, car_model_id: int):
        self._dao.insert_into_order_car_with_checks(order_id, car_length, car_width, car_engine_id,
                                                    car_body_id, car_body_type, car_chassis_id, car_drive_id,
                                                    car_photo_id, car_model_id)
