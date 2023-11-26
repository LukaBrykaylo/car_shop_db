from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import drive_controller
from t08_flask_mysql.app.my_project.auth.domain import Drive

drive_bp = Blueprint('drives', __name__, url_prefix='/drives')

@drive_bp.get('')
def get_all_drives() -> Response:
    return make_response(jsonify(drive_controller.find_all()), HTTPStatus.OK)

@drive_bp.post('')
def create_drive() -> Response:
    content = request.get_json()
    drive = Drive.create_from_dto(content)
    drive_controller.create(drive)
    return make_response(jsonify(drive.put_into_dto()), HTTPStatus.CREATED)

@drive_bp.get('/<int:drive_id>')
def get_drive(drive_id: int) -> Response:
    return make_response(jsonify(drive_controller.find_by_id(drive_id)), HTTPStatus.OK)

@drive_bp.put('/<int:drive_id>')
def update_drive(drive_id: int) -> Response:
    content = request.get_json()
    drive = Drive.create_from_dto(content)
    drive_controller.update(drive_id, drive)
    return make_response("Drive updated", HTTPStatus.OK)

@drive_bp.patch('/<int:drive_id>')
def patch_drive(drive_id: int) -> Response:
    content = request.get_json()
    drive_controller.patch(drive_id, content)
    return make_response("Drive updated", HTTPStatus.OK)

@drive_bp.delete('/<int:drive_id>')
def delete_drive(drive_id: int) -> Response:
    drive_controller.delete(drive_id)
    return make_response("Drive deleted", HTTPStatus.OK)
