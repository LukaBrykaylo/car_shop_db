from t08_flask_mysql.app.my_project.auth.service import engine_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class EngineController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = engine_service

    def dynamic_table(self):
        self._service.dynamic_table()
