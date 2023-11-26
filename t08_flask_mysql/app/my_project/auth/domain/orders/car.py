from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto
from t08_flask_mysql.app.my_project.auth.domain.orders.body import Body
from t08_flask_mysql.app.my_project.auth.domain.orders.chassis import Chassis
from t08_flask_mysql.app.my_project.auth.domain.orders.drive import Drive
from t08_flask_mysql.app.my_project.auth.domain.orders.engine import Engine
from t08_flask_mysql.app.my_project.auth.domain.orders.model import Model
from t08_flask_mysql.app.my_project.auth.domain.orders.photo import Photo

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
            "chassis": self.chassis_id,
            "drive": self.drive_id,
            "photo": self.photo_id,
            "model": self.model_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Car:
        # Creating a Car object from DTO may require handling relationships
        # You might want to extract data for 'engine', 'body', etc., and create related objects
        # For simplicity, assuming relationships are not provided in the DTO
        return Car(
            length=dto_dict.get("length"),
            width=dto_dict.get("width"),
            engine=Engine.dto_dict.get("engine_id"),
            body=Body.dto_dict.get("body_id"),
            chassis=Chassis.dto_dict.get("chassis_id"),
            drive=Drive.dto_dict.get("drive_id"),
            photo=Photo.dto_dict.get("photo_id"),
            model=Model.dto_dict.get("model_id"),
        )