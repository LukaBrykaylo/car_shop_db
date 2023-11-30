from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Order
from t08_flask_mysql.app.my_project.auth.domain import Car
from t08_flask_mysql.app.my_project.auth.domain.orders.order import order_has_car


class OrderDAO(GeneralDAO):
    _domain_type = Order

    # def add_order_to_car(self, order_id: int, car_id: int):
    #     session = self.get_session()


    def find_cars(self, order_id: int):
        """
        Find solar system associated with a specific order.
        :param order_id: ID of the order
        :return: List of SolarSystem objects associated with the order
        """
        # Assuming that you have a session object, replace it with your actual SQLAlchemy session
        session = self.get_session()

        order = session.query(Order).filter_by(id=order_id).first()

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

        order_data = {
            "order": order.put_into_dto(),
            "cars": [car.put_into_dto() for car in cars]
        }

        return order_data

    def add_car_to_order(self, order_id: int, car_id: int):
        session = self.get_session()

        association = order_has_car.insert().values(
            order_id=order_id,
            car_id=car_id
        )

        session.execute(association)

        session.commit()

    def remove_car_from_order_id(self, order_id: int, car_id: int):
        session = self.get_session()

        session.execute(
            order_has_car.delete()
            .where(order_has_car.c.order_id == order_id)
            .where(order_has_car.c.car_id == car_id)
        )

        session.commit()
