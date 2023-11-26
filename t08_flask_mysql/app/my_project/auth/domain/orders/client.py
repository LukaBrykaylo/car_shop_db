from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto

class Client(db.Model, IDto):
    __tablename__ = "client"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(45), nullable=False)
    phone = db.Column(db.DECIMAL, nullable=False)
    age = db.Column(db.Integer)

    def __repr__(self) -> str:
        return f"Client({self.id}, '{self.name}', '{self.surname}', {self.phone}, {self.age})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "phone": self.phone,
            "age": self.age,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Client:
        return Client(
            name=dto_dict.get("name"),
            surname=dto_dict.get("surname"),
            phone=dto_dict.get("phone"),
            age=dto_dict.get("age"),
        )
