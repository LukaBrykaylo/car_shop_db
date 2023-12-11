from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import comment_controller
from t08_flask_mysql.app.my_project.auth.domain import Comment

comment_bp = Blueprint('comments', __name__, url_prefix='/comments')

@comment_bp.get('')
def get_all_comments() -> Response:
    return make_response(jsonify(comment_controller.find_all()), HTTPStatus.OK)

@comment_bp.post('')
def create_comment() -> Response:
    content = request.get_json()
    comment = Comment.create_from_dto(content)
    comment_controller.create(comment)
    return make_response(jsonify(comment.put_into_dto()), HTTPStatus.CREATED)

@comment_bp.get('/<int:comment_id>')
def get_comment(comment_id: int) -> Response:
    return make_response(jsonify(comment_controller.find_by_id(comment_id)), HTTPStatus.OK)

@comment_bp.put('/<int:comment_id>')
def update_comment(comment_id: int) -> Response:
    content = request.get_json()
    comment = Comment.create_from_dto(content)
    comment_controller.update(comment_id, comment)
    return make_response("Comment updated", HTTPStatus.OK)

@comment_bp.patch('/<int:comment_id>')
def patch_comment(comment_id: int) -> Response:
    content = request.get_json()
    comment_controller.patch(comment_id, content)
    return make_response("Comment updated", HTTPStatus.OK)

@comment_bp.delete('/<int:comment_id>')
def delete_comment(comment_id: int) -> Response:
    comment_controller.delete(comment_id)
    return make_response("Comment deleted", HTTPStatus.OK)

@comment_bp.get('/get_rate_value/<comments_value_by>')
def get_comment_value(comments_value_by: str) -> Response:
    return make_response(jsonify(comment_controller.get_comment_value(comments_value_by)), HTTPStatus.OK)
