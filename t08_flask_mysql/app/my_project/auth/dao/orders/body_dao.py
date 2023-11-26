from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Body


class BodyDAO(GeneralDAO):
    _domain_type = Body

    def find_by_type(self, body_type: str) -> List[Body]:
        return self._session.query(Body).filter(Body.body_type == body_type).all()
