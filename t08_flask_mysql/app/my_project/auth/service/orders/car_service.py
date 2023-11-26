from t08_flask_mysql.app.my_project.auth.dao import car_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class CarService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = car_dao
