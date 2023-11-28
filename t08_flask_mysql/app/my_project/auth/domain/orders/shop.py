from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto
from t08_flask_mysql.app.my_project.auth.domain.orders.city import City
from t08_flask_mysql.app.my_project.auth.domain.orders.comment import Comment

class Shop(db.Model, IDto):
    __tablename__ = "shop"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cars_number = db.Column(db.Integer, nullable=False)
    street_address = db.Column(db.String(45), nullable=False)
    phone = db.Column(db.DECIMAL, nullable=False, unique=True)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'), nullable=False)

    city = db.relationship('City', backref='shops')
    comment = db.relationship('Comment', backref='shops')

    def __repr__(self) -> str:
        return f"Shop({self.id}, {self.cars_number}, {self.street_address}, {self.phone}, {self.city}, {self.comment})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "cars_number": self.cars_number,
            "street_address": self.street_address,
            "phone": self.phone,
            "city": self.city_id,
            "comment": self.comment_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Shop:
        return Shop(
            cars_number=dto_dict.get("cars_number"),
            street_address=dto_dict.get("street_address"),
            phone=dto_dict.get("phone"),
            city_id=dto_dict.get("city"),
            comment_id=dto_dict.get("comment"),
        )
