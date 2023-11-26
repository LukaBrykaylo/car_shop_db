from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Engine


class EngineDAO(GeneralDAO):
    _domain_type = Engine

    def find_by_name(self, engine_name: str) -> List[Engine]:
        return self._session.query(Engine).filter(Engine.name == engine_name).all()

    def find_by_horse_power_range(self, min_power: int, max_power: int) -> List[Engine]:
        return self._session.query(Engine).filter(Engine.horse_power.between(min_power, max_power)).all()
