from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Comment
from t08_flask_mysql.app.my_project.auth.domain.orders.car import Car


class CommentDAO(GeneralDAO):
    _domain_type = Comment

    def find_by_name(self, commenter_name: str) -> List[Comment]:
        return self._session.query(Comment).filter(Comment.name == commenter_name).all()

    def find_by_rate_range(self, min_rate: int, max_rate: int) -> List[Comment]:
        return self._session.query(Comment).filter(Comment.rate.between(min_rate, max_rate)).all()

    def get_comments_for_car(self, car_id: int) -> List[Comment]:
        return (
            self._session.query(Comment)
            .join(Car, Car.comments)
            .filter(Car.id == car_id)
            .all()
        )
