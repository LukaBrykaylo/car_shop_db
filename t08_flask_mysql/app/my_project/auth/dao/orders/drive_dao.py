from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Drive


class DriveDAO(GeneralDAO):
    _domain_type = Drive

    def find_by_4wd(self, is_4wd: bool) -> List[Drive]:
        return self._session.query(Drive).filter(Drive.is_4WD == is_4wd).all()
