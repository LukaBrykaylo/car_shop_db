from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Photo


class PhotoDAO(GeneralDAO):
    _domain_type = Photo

    # def find_by_id(self, photo_id: int) -> List[Photo]:
    #     return self._session.query(Photo).filter(Photo.id == photo_id).all()
