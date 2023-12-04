from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import chassis_controller
from t08_flask_mysql.app.my_project.auth.domain import Chassis

chassis_bp = Blueprint('chassis', __name__, url_prefix='/chassis')

@chassis_bp.get('')
def get_all_chassis() -> Response:
    return make_response(jsonify(chassis_controller.find_all()), HTTPStatus.OK)

@chassis_bp.post('')
def create_chassis() -> Response:
    content = request.get_json()
    chassis = Chassis.create_from_dto(content)
    chassis_controller.create(chassis)
    return make_response(jsonify(chassis.put_into_dto()), HTTPStatus.CREATED)

@chassis_bp.get('/<int:chassis_id>')
def get_chassis(chassis_id: int) -> Response:
    return make_response(jsonify(chassis_controller.find_by_id(chassis_id)), HTTPStatus.OK)

@chassis_bp.put('/<int:chassis_id>')
def update_chassis(chassis_id: int) -> Response:
    content = request.get_json()
    chassis = Chassis.create_from_dto(content)
    chassis_controller.update(chassis_id, chassis)
    return make_response("Chassis updated", HTTPStatus.OK)

@chassis_bp.patch('/<int:chassis_id>')
def patch_chassis(chassis_id: int) -> Response:
    content = request.get_json()
    chassis_controller.patch(chassis_id, content)
    return make_response("Chassis updated", HTTPStatus.OK)

@chassis_bp.delete('/<int:chassis_id>')
def delete_chassis(chassis_id: int) -> Response:
    chassis_controller.delete(chassis_id)
    return make_response("Chassis deleted", HTTPStatus.OK)

@chassis_bp.post('/insert_chassis')
def insert_into_chassis() -> Response:
    content = request.get_json()
    chassis_model = content.get('chassis_model')
    chassis_wheel_number = content.get('chassis_wheel_number')

    chassis_controller.insert_into_chassis(chassis_model, chassis_wheel_number)
    return make_response('chassis added', HTTPStatus.CREATED)
