from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Photo(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "photo"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image = db.Column(db.String(30), nullable=True)

    def __repr__(self) -> str:
        return f"Photo({self.id}, {self.image})"
    
    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "image": self.image
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Photo:
        return Photo(
            image=dto_dict.get("image"),
        )
