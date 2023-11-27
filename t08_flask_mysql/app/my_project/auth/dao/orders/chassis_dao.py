from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Chassis


class ChassisDAO(GeneralDAO):
    _domain_type = Chassis

    # def find_by_model(self, model: str) -> List[Chassis]:
    #     return self._session.query(Chassis).filter(Chassis.model == model).all()
