from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO

from t08_flask_mysql.app.my_project.auth.domain import City
from t08_flask_mysql.app.my_project.auth.domain.orders.car import Car
from t08_flask_mysql.app.my_project.auth.domain.orders.shop import Shop


class CityDAO(GeneralDAO):
    _domain_type = City

    def find_by_name(self, city_name: str) -> List[City]:
        return self._session.query(City).filter(City.name == city_name).all()

    def get_cars_in_city(self, city_name: str) -> List[Car]:
        return (
            self._session.query(Car)
            .join(Shop, Shop.cars)
            .join(City)
            .filter(City.name == city_name)
            .all()
        )

    def find_shops_by_index(self, index: int) -> List[Shop]:
        """
        Gets all shops in the city by city index.
        :param index: city index
        :return: list of shops
        """
        # Отримати місто за індексом
        city = self._session.query(City).filter(City.id == index).first()

        if city:
            # Отримати всі магазини, які мають city_id, яке відповідає індексу міста
            shops = self._session.query(Shop).filter(Shop.city_id == city.id).all()
            return [shop.put_into_dto() for shop in shops]
        return []
