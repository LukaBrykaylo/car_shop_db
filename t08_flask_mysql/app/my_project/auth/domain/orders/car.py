from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto

class Car(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "car"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    length = db.Column(db.Integer, nullable=False)
    width = db.Column(db.Integer, nullable=False)
    engine_id = db.Column(db.Integer, db.ForeignKey('engine.id'), nullable=False)
    body_id = db.Column(db.Integer, db.ForeignKey('body.id'), nullable=False)
    body_body_type = db.Column(db.String(45), nullable=False)
    chassis_id = db.Column(db.Integer, db.ForeignKey('chassis.id'), nullable=False)
    drive_id = db.Column(db.Integer, db.ForeignKey('drive.id'), nullable=False)
    photo_id = db.Column(db.Integer, db.ForeignKey('photo.id'), nullable=False)
    model_id = db.Column(db.Integer, db.ForeignKey('model.id'), nullable=False)

    engine = db.relationship('Engine', backref='cars')
    body = db.relationship('Body', backref='cars')
    chassis = db.relationship('Chassis', backref='cars')
    drive = db.relationship('Drive', backref='cars')
    photo = db.relationship('Photo', backref='cars')
    model = db.relationship('Model', backref='cars')

    def __repr__(self) -> str:
        return f"Car({self.id}, {self.length}, {self.width}, {self.engine}, {self.body}, {self.chassis}, {self.drive}, {self.photo}, {self.model})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "length": self.length,
            "width": self.width,
            "engine": self.engine_id,
            "body": self.body_id,
            "body_type": self.body_body_type,
            "chassis": self.chassis_id,
            "drive": self.drive_id,
            "photo": self.photo_id,
            "model": self.model_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Car:
        return Car(
            length=dto_dict.get("length"),
            width=dto_dict.get("width"),
            engine_id=dto_dict.get("engine"),
            body_id=dto_dict.get("body"),
            body_body_type=dto_dict.get("body_type"),
            chassis_id=dto_dict.get("chassis"),
            drive_id=dto_dict.get("drive"),
            photo_id=dto_dict.get("photo"),
            model_id=dto_dict.get("model"),
        )
