from t08_flask_mysql.app.my_project.auth.service import model_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class ModelController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = model_service
