from sqlalchemy import text

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Engine


class EngineDAO(GeneralDAO):
    _domain_type = Engine

    def dynamic_table(self):
        try:
            self.get_session().execute(text("CALL dynamic_table()"))
            self.get_session().commit()
        except Exception as e:
            print(f"Error: {e}")
