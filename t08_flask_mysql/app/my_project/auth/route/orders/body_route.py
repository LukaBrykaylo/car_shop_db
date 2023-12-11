from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import body_controller
from t08_flask_mysql.app.my_project.auth.domain import Body

body_bp = Blueprint('bodies', __name__, url_prefix='/bodies')

@body_bp.get('')
def get_all_bodies() -> Response:
    return make_response(jsonify(body_controller.find_all()), HTTPStatus.OK)

@body_bp.post('')
def create_body() -> Response:
    content = request.get_json()
    body = Body.create_from_dto(content)
    body_controller.create(body)
    return make_response(jsonify(body.put_into_dto()), HTTPStatus.CREATED)

@body_bp.get('/<int:body_id>')
def get_body(body_id: int) -> Response:
    return make_response(jsonify(body_controller.find_by_id(body_id)), HTTPStatus.OK)

@body_bp.put('/<int:body_id>')
def update_body(body_id: int) -> Response:
    content = request.get_json()
    body = Body.create_from_dto(content)
    body_controller.update(body_id, body)
    return make_response("Body updated", HTTPStatus.OK)

@body_bp.patch('/<int:body_id>')
def patch_body(body_id: int) -> Response:
    content = request.get_json()
    body_controller.patch(body_id, content)
    return make_response("Body updated", HTTPStatus.OK)

@body_bp.delete('/<int:body_id>')
def delete_body(body_id: int) -> Response:
    body_controller.delete(body_id)
    return make_response("Body deleted", HTTPStatus.OK)
