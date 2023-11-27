from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Order


class OrderDAO(GeneralDAO):
    _domain_type = Order

    # def find_by_client_id(self, client_id: int) -> List[Order]:
    #     return self._session.query(Order).filter(Order.client_id == client_id).all()
    #
    # def find_by_shop_id(self, shop_id: int) -> List[Order]:
    #     return self._session.query(Order).filter(Order.shop_id == shop_id).all()
