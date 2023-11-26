from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import model_controller
from t08_flask_mysql.app.my_project.auth.domain import Model

model_bp = Blueprint('models', __name__, url_prefix='/models')

@model_bp.get('')
def get_all_models() -> Response:
    return make_response(jsonify(model_controller.find_all()), HTTPStatus.OK)

@model_bp.post('')
def create_model() -> Response:
    content = request.get_json()
    model = Model.create_from_dto(content)
    model_controller.create(model)
    return make_response(jsonify(model.put_into_dto()), HTTPStatus.CREATED)

@model_bp.get('/<int:model_id>')
def get_model(model_id: int) -> Response:
    return make_response(jsonify(model_controller.find_by_id(model_id)), HTTPStatus.OK)

@model_bp.put('/<int:model_id>')
def update_model(model_id: int) -> Response:
    content = request.get_json()
    model = Model.create_from_dto(content)
    model_controller.update(model_id, model)
    return make_response("Model updated", HTTPStatus.OK)

@model_bp.patch('/<int:model_id>')
def patch_model(model_id: int) -> Response:
    content = request.get_json()
    model_controller.patch(model_id, content)
    return make_response("Model updated", HTTPStatus.OK)

@model_bp.delete('/<int:model_id>')
def delete_model(model_id: int) -> Response:
    model_controller.delete(model_id)
    return make_response("Model deleted", HTTPStatus.OK)
