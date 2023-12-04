from t08_flask_mysql.app.my_project.auth.service import comment_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController
from typing import List


class CommentController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = comment_service

    def get_comment_value(self, comments_value_by: str) -> List[object]:
        return list(map(lambda x: dict(x), self._service.get_comment_value(comments_value_by)))