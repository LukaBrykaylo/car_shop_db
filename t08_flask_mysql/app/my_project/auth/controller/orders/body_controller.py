from t08_flask_mysql.app.my_project.auth.service import body_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class BodyController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = body_service
