from t08_flask_mysql.app.my_project.auth.service import comment_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class CommentController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = comment_service
