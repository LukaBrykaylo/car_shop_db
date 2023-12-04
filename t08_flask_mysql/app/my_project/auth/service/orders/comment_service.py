from t08_flask_mysql.app.my_project.auth.dao import comment_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService
from typing import List

class CommentService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = comment_dao

    def get_comment_value(self, comments_value_by: str) -> List[object]:
        return self._dao.get_comment_value(comments_value_by)
