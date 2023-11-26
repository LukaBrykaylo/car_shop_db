from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto

class Chassis(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "chassis"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    model = db.Column(db.String(45), nullable=False)
    wheel_number = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"Chassis({self.id}, '{self.model}', {self.wheel_number})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "model": self.model,
            "wheel_number": self.wheel_number,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Chassis:
        return Chassis(
            model=dto_dict.get("model"),
            wheel_number=dto_dict.get("wheel_number"),
        )