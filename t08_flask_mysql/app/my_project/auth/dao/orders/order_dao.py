from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Order
from t08_flask_mysql.app.my_project.auth.domain import Car
from t08_flask_mysql.app.my_project.auth.domain.orders.order import order_has_car


class OrderDAO(GeneralDAO):
    _domain_type = Order

    def find_cars(self, order_id: int):
        """
        Find solar system associated with a specific order.
        :param order_id: ID of the order
        :return: List of SolarSystem objects associated with the order
        """
        # Assuming that you have a session object, replace it with your actual SQLAlchemy session
        session = self.get_session()

        # Query the association table to get the solar system IDs associated with the order
        cars_ids = (
            session.query(order_has_car.c.car_id)
            .filter(order_has_car.c.order_id == order_id)
            .all()
        )

        # Extract solar system IDs from the result
        car_ids = [car_id for (car_id,) in cars_ids]

        # Query the SolarSystem table to get the SolarSystem objects associated with the solar system IDs
        cars = session.query(Car).filter(Car.id.in_(car_ids)).all()

        return [car.put_into_dto() for car in cars]
