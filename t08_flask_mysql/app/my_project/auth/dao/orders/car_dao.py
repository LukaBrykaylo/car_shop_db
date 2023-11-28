from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Car
from t08_flask_mysql.app.my_project.auth.domain import Order
from t08_flask_mysql.app.my_project.auth.domain.orders.order import order_has_car


class CarDAO(GeneralDAO):
    _domain_type = Car

    def find_orders(self, car_id: int):
        """
        Find order associated with a specific solar system.
        :param car_id: ID of the solar system
        :return: List of Order objects associated with the solar system
        """
        # Assuming that you have a session object, replace it with your actual SQLAlchemy session
        session = self.get_session()

        # Query the association table to get the order IDs associated with the solar system
        orders_ids = (
            session.query(order_has_car.c.order_id)
            .filter(order_has_car.c.car_id == car_id)
            .all()
        )

        # Extract order IDs from the result
        order_ids = [order_id for (order_id,) in orders_ids]

        # Query the Order table to get the Order objects associated with the order IDs
        orders = session.query(Order).filter(Order.id.in_(order_ids)).all()

        return [order.put_into_dto() for order in orders]