from t08_flask_mysql.app.my_project.auth.dao import shop_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class ShopService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = shop_dao
