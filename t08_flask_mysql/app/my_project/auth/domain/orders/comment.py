from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto

class Comment(db.Model, IDto):
    __tablename__ = "comment"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45))
    comment_text = db.Column(db.String(300), nullable=False)
    rate = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"Comment({self.id}, '{self.name}', '{self.comment_text}', {self.rate})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "comment_text": self.comment_text,
            "rate": self.rate,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Comment:
        return Comment(
            name=dto_dict.get("name"),
            comment_text=dto_dict.get("comment_text"),
            rate=dto_dict.get("rate"),
        )
