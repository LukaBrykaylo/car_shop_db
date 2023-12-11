from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import OrderCar
from t08_flask_mysql.app.my_project.auth.domain import Car
from t08_flask_mysql.app.my_project.auth.domain import Order


class OrderCarDAO(GeneralDAO):
    _domain_type = OrderCar

    def find_cars_by_order_id(self, order_id: int) -> List[Car]:
        """
        Gets all cars associated with a specific order.
        :param order_id: Order ID
        :return: list of cars
        """
        order_cars = self._session.query(OrderCar).filter(OrderCar.order_id == order_id).all()
        if order_cars:
            car_ids = [ocar.car_id for ocar in order_cars]
            cars = self._session.query(Car).filter(Car.id.in_(car_ids)).all()
            return [car.put_into_dto() for car in cars]
        return []

    def find_orders_by_car_id(self, car_id: int) -> List[Order]:
        """
        Gets all orders associated with a specific car.
        :param car_id: Car ID
        :return: list of orders
        """
        order_cars = self._session.query(OrderCar).filter(OrderCar.car_id == car_id).all()

        if order_cars:
            order_ids = [oord.order_id for oord in order_cars]
            orders = self._session.query(Order).filter(Order.id.in_(order_ids)).all()
            return [order.put_into_dto() for order in orders]
        return []
