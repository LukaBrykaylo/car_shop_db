from sqlalchemy import text
from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Photo


class PhotoDAO(GeneralDAO):
    _domain_type = Photo

    def add_ten_photos(self):
        try:
            # sql_express = text("CALL insert_10_into_photo()")
            self.get_session().execute(text("CALL insert_10_into_photo()"))
            self.get_session().commit()
        except Exception as e:
            print(f"Error: {e}")
