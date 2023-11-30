from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto
from t08_flask_mysql.app.my_project.auth.domain.orders.client import Client
from t08_flask_mysql.app.my_project.auth.domain.orders.shop import Shop

order_has_car = db.Table(
    'order_has_car',
    db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key=True),
    db.Column('car_id', db.Integer, db.ForeignKey('car.id'), primary_key=True),
    db.UniqueConstraint('order_id', 'car_id', name='uq_order_has_car'),
    extend_existing=True
)


class Order(db.Model, IDto):
    __tablename__ = "order"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    shop_id = db.Column(db.Integer, db.ForeignKey('shop.id'), nullable=False)
    order_time = db.Column(db.Date, nullable=False)
    # all_cars = []

    client = db.relationship('Client', backref='orders')
    shop = db.relationship('Shop', backref='orders')

    # Relationship M:M with Order
    cars = db.relationship("Car", secondary="order_has_car", back_populates="orders")

    def __repr__(self) -> str:
        return f"Order({self.id}, {self.client}, {self.shop}, {self.order_time})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "client": self.client_id,
            "shop": self.shop_id,
            "order_time": self.order_time.isoformat(),  # Convert Date to ISO format for serialization
            # "all_cars": self.all_cars,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Order:
        return Order(
            order_time=dto_dict.get("order_time"),
            client_id=dto_dict.get("client"),
            shop_id=dto_dict.get("shop"),
            # all_cars=dto_dict.get("all_cars"),
        )
