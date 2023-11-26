from t08_flask_mysql.app.my_project.auth.dao import comment_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class CommentService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = comment_dao
