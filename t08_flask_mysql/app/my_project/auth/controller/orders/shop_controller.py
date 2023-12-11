from t08_flask_mysql.app.my_project.auth.service import shop_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class ShopController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = shop_service
