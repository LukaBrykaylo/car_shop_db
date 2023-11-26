from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import TestDrive


class TestDriveDAO(GeneralDAO):
    _domain_type = TestDrive

    def find_by_client_id(self, client_id: int) -> List[TestDrive]:
        return self._session.query(TestDrive).filter(TestDrive.client_id == client_id).all()

    def find_by_car_id(self, car_id: int) -> List[TestDrive]:
        return self._session.query(TestDrive).filter(TestDrive.car_id == car_id).all()

    def find_by_comment_id(self, comment_id: int) -> List[TestDrive]:
        return self._session.query(TestDrive).filter(TestDrive.comment_id == comment_id).all()
