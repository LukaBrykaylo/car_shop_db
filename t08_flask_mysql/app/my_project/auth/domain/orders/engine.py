from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto

class Engine(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "engine"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    horse_power = db.Column(db.Integer, nullable=False)
    max_speed = db.Column(db.Integer, nullable=False)
    manual = db.Column(db.Boolean, nullable=False)

    def __repr__(self) -> str:
        return f"ClientType({self.id}, '{self.name}, {self.horse_power}, {self.max_speed}, {self.manual}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "horse_power": self.horse_power,
            "max_speed": self.max_speed,
            "manual": self.manual,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Engine:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Engine(
            name=dto_dict.get("name"),
            horse_power=dto_dict.get("horse_power"),
            max_speed=dto_dict.get("max_speed"),
            manual=dto_dict.get("manual"),
        )
        return obj