from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto
from t08_flask_mysql.app.my_project.auth.domain.orders.car import Car
from t08_flask_mysql.app.my_project.auth.domain.orders.client import Client
from t08_flask_mysql.app.my_project.auth.domain.orders.comment import Comment

class TestDrive(db.Model, IDto):
    __tablename__ = "test_drive"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'), nullable=False)

    client = db.relationship('Client', backref='test_drives')
    car = db.relationship('Car', backref='test_drives')
    comment = db.relationship('Comment', backref='test_drives')

    def __repr__(self) -> str:
        return f"TestDrive({self.id}, {self.client}, {self.car}, {self.comment})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "client": self.client.put_into_dto(),
            "car": self.car.put_into_dto(),
            "comment": self.comment.put_into_dto(),
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> TestDrive:
        # Creating a TestDrive object from DTO may require handling relationships
        # You might want to extract data for 'client', 'car', and 'comment' and create related objects
        # For simplicity, assuming relationships are not provided in the DTO
        return TestDrive(
            client=Client.create_from_dto(dto_dict.get("client", {})),
            car=Car.create_from_dto(dto_dict.get("car", {})),
            comment=Comment.create_from_dto(dto_dict.get("comment", {})),
        )
