from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto
from t08_flask_mysql.app.my_project.auth.domain.orders.shop import Shop


class City(db.Model, IDto):
    __tablename__ = "city"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    shops_in_city = db.relationship('Shop', backref='cities', lazy=True)

    def __repr__(self) -> str:
        return f"City({self.id}, '{self.name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "shops_in_city":  [shop.put_into_dto() for shop in self.shops_in_city],
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> City:
        shop_ids = dto_dict.get("shops_in_city", [])
        # print(shop_ids)
        # shops = Shop.query.filter(Shop.id.in_(shop_ids)).all()

        return City(
            name=dto_dict.get("name"),
            shops_in_city=shop_ids,
        )
