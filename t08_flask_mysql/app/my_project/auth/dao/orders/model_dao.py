from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Model


class ModelDAO(GeneralDAO):
    _domain_type = Model

    def find_by_name(self, model_name: str) -> List[Model]:
        return self._session.query(Model).filter(Model.model_name == model_name).all()
