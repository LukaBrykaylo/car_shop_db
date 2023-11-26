from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto
from t08_flask_mysql.app.my_project.auth.domain.orders.car import Car
from t08_flask_mysql.app.my_project.auth.domain.orders.order import Order

class OrderCar(db.Model, IDto):
    __tablename__ = "order_car"

    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), primary_key=True, nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), primary_key=True, nullable=False)
    number = db.Column(db.Integer, nullable=False)

    order = db.relationship('Order', backref='order_cars')
    car = db.relationship('Car', backref='order_cars')

    def __repr__(self) -> str:
        return f"OrderCar({self.order}, {self.car}, {self.number})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "order": self.order_id,
            "car": self.car_id,
            "number": self.number,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> OrderCar:
        # Creating an OrderCar object from DTO may require handling relationships
        # You might want to extract data for 'order' and 'car' and create related objects
        # For simplicity, assuming relationships are not provided in the DTO
        return OrderCar(
            number=dto_dict.get("number"),
            order=Order.dto_dict.get("order"),
            car=Car.dto_dict.get("car"),
        )
