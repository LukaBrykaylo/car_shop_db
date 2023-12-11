from sqlalchemy import text

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

    def insert_into_order_car_with_checks(self, order_id: int, car_length:int, car_width: int, car_engine_id: int,
                                          car_body_id: int, car_body_type: str, car_chassis_id: int, car_drive_id: int,
                                          car_photo_id: int, car_model_id: int):
        try:
            self.get_session().execute(text("CALL insert_into_order_car_with_checks(:order_id, :car_length, "
            ":car_width, :car_engine_id, :car_body_id, :car_body_type, :car_chassis_id, :car_drive_id, "
            ":car_photo_id, :car_model_id)"),
                                       {
                                           'order_id': order_id,
                                           'car_length': car_length,
                                           'car_width': car_width,
                                           'car_engine_id': car_engine_id,
                                           'car_body_id': car_body_id,
                                           'car_body_type': car_body_type,
                                           'car_chassis_id': car_chassis_id,
                                           'car_drive_id': car_drive_id,
                                           'car_photo_id': car_photo_id,
                                           'car_model_id': car_model_id
                                       }
                                       )
            self.get_session().commit()
        except Exception as e:
            print(f"Error: {e}")
