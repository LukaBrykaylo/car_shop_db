from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Car
from t08_flask_mysql.app.my_project.auth.domain.orders.body import Body
from t08_flask_mysql.app.my_project.auth.domain.orders.chassis import Chassis
from t08_flask_mysql.app.my_project.auth.domain.orders.drive import Drive
from t08_flask_mysql.app.my_project.auth.domain.orders.model import Model


class CarDAO(GeneralDAO):
    _domain_type = Car

    # def find_by_model(self, model_name: str) -> List[Car]:
    #     return self._session.query(Car).join(Car.model).filter(Model.model_name == model_name).all()
    #
    # def find_by_engine_power(self, min_power: int, max_power: int) -> List[Car]:
    #     return self._session.query(Car).join(Car.engine).filter(Car.engine.horse_power.between(min_power, max_power)).all()
    #
    # def find_by_body_type(self, body_type: str) -> List[Car]:
    #     return self._session.query(Car).join(Car.body).filter(Body.body_type == body_type).all()
    #
    # def find_by_chassis_model(self, chassis_model: str) -> List[Car]:
    #     return self._session.query(Car).join(Car.chassis).filter(Chassis.model == chassis_model).all()
    #
    # def find_by_drive_type(self, is_4wd: bool) -> List[Car]:
    #     return self._session.query(Car).join(Car.drive).filter(Drive.is_4WD == is_4wd).all()

