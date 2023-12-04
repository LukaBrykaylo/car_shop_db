from typing import List

import sqlalchemy

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Comment


class CommentDAO(GeneralDAO):
    _domain_type = Comment

    def get_comment_value(self, comments_value_by: str) -> List[object]:
        return self._session.execute(sqlalchemy.text("CALL call_get_comment_value(:comments_value_by)"),
                                     {"comments_value_by": comments_value_by}).mappings().all()
