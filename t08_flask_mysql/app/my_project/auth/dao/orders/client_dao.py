from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Client


class ClientDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = Client

    def find_by_name(self, name: str) -> List[object]:
        """
        Gets Client objects from database table by field name.
        :param name: name value
        :return: search objects
        """
        return self._session.query(Client).filter(Client.name == name).order_by(Client.name).all()

    def find_by_number(self, phone: int) -> List[object]:
        """
        Gets Client objects from database table by field 'number'.
        :param number: number value
        :return: search objects
        """
        return self._session.query(Client).filter(Client.phone == phone).all()