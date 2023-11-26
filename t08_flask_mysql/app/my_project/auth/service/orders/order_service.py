from t08_flask_mysql.app.my_project.auth.dao import order_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class OrderService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = order_dao
