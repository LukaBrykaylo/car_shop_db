from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Body(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "body"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    body_type = db.Column(db.String(45), primary_key=True, nullable=False)
    seats = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(45), nullable=False)
    is_leather = db.Column(db.Boolean, nullable=False)

    def __repr__(self) -> str:
        return f"Body({self.id}, '{self.body_type}', {self.seats}, '{self.color}', {self.is_leather})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "body_type": self.body_type,
            "seats": self.seats,
            "color": self.color,
            "is_leather": self.is_leather,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Body:
        return Body(
            body_type=dto_dict.get("body_type"),
            seats=dto_dict.get("seats"),
            color=dto_dict.get("color"),
            is_leather=dto_dict.get("is_leather"),
        )
