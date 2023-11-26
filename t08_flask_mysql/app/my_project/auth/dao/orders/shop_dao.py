from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Shop
from t08_flask_mysql.app.my_project.auth.domain import Comment
from t08_flask_mysql.app.my_project.auth.domain.orders.city import City


class ShopDAO(GeneralDAO):
    _domain_type = Shop

    def find_by_cars_number(self, cars_number: int) -> List[Shop]:
        return self._session.query(Shop).filter(Shop.cars_number == cars_number).all()

    def find_by_city(self, city_name: str) -> List[Shop]:
        return (
            self._session.query(Shop)
            .join(City)
            .filter(City.name == city_name)
            .all()
        )

    def find_by_phone(self, phone: float) -> List[Shop]:
        return self._session.query(Shop).filter(Shop.phone == phone).all()
