from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto

class Model(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "model"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    model_name = db.Column(db.String(45), nullable=False)

    def __repr__(self) -> str:
        return f"Model({self.id}, '{self.model_name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "model_name": self.model_name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Model:
        return Model(
            model_name=dto_dict.get("model_name"),
        )
