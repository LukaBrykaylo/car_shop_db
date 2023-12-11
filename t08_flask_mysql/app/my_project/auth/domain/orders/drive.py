from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto

class Drive(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "drive"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    is_4WD = db.Column(db.Boolean, nullable=False)
    wheel_number = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"Drive({self.id}, {self.is_4WD}, {self.wheel_number})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "is_4WD": self.is_4WD,
            "wheel_number": self.wheel_number,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Drive:
        return Drive(
            is_4WD=dto_dict.get("is_4WD"),
            wheel_number=dto_dict.get("wheel_number"),
        )
