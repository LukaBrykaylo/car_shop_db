from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto
from t08_flask_mysql.app.my_project.auth.domain.orders.client import Client
from t08_flask_mysql.app.my_project.auth.domain.orders.shop import Shop

class Order(db.Model, IDto):
    __tablename__ = "order"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    shop_id = db.Column(db.Integer, db.ForeignKey('shop.id'), nullable=False)
    order_time = db.Column(db.Date, nullable=False)

    client = db.relationship('Client', backref='orders')
    shop = db.relationship('Shop', backref='orders')

    def __repr__(self) -> str:
        return f"Order({self.id}, {self.client}, {self.shop}, {self.order_time})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "client": self.client_id,
            "shop": self.shop_id,
            "order_time": self.order_time.isoformat(),  # Convert Date to ISO format for serialization
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Order:
        # Creating an Order object from DTO may require handling relationships
        # You might want to extract data for 'client' and 'shop' and create related objects
        # For simplicity, assuming relationships are not provided in the DTO
        return Order(
            order_time=dto_dict.get("order_time"),
            client=Client.dto_dict.get("client"),
            shop=Shop.dto_dict.get("shop"),
        )