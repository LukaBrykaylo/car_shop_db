from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import engine_controller
from t08_flask_mysql.app.my_project.auth.domain import Engine

engine_bp = Blueprint('engines', __name__, url_prefix='/engines')

@engine_bp.get('')
def get_all_engines() -> Response:
    return make_response(jsonify(engine_controller.find_all()), HTTPStatus.OK)

@engine_bp.post('')
def create_engine() -> Response:
    content = request.get_json()
    engine = Engine.create_from_dto(content)
    engine_controller.create(engine)
    return make_response(jsonify(engine.put_into_dto()), HTTPStatus.CREATED)

@engine_bp.get('/<int:engine_id>')
def get_engine(engine_id: int) -> Response:
    return make_response(jsonify(engine_controller.find_by_id(engine_id)), HTTPStatus.OK)

@engine_bp.put('/<int:engine_id>')
def update_engine(engine_id: int) -> Response:
    content = request.get_json()
    engine = Engine.create_from_dto(content)
    engine_controller.update(engine_id, engine)
    return make_response("Engine updated", HTTPStatus.OK)

@engine_bp.patch('/<int:engine_id>')
def patch_engine(engine_id: int) -> Response:
    content = request.get_json()
    engine_controller.patch(engine_id, content)
    return make_response("Engine updated", HTTPStatus.OK)

@engine_bp.delete('/<int:engine_id>')
def delete_engine(engine_id: int) -> Response:
    engine_controller.delete(engine_id)
    return make_response("Engine deleted", HTTPStatus.OK)

@engine_bp.post('/dynamic_table')
def dynamic_table() -> Response:
    engine_controller.dynamic_table()
    return make_response("Dynamic table created", HTTPStatus.CREATED)