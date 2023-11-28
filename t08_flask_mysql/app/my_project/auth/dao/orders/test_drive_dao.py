from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import TestDrive


class TestDriveDAO(GeneralDAO):
    _domain_type = TestDrive
