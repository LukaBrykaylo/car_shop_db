from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import photo_controller
from t08_flask_mysql.app.my_project.auth.domain import Photo

photo_bp = Blueprint('photos', __name__, url_prefix='/photos')

@photo_bp.get('')
def get_all_photos() -> Response:
    return make_response(jsonify(photo_controller.find_all()), HTTPStatus.OK)

@photo_bp.post('')
def create_photo() -> Response:
    content = request.get_json()
    photo = Photo.create_from_dto(content)
    photo_controller.create(photo)
    return make_response(jsonify(photo.put_into_dto()), HTTPStatus.CREATED)

@photo_bp.get('/<int:photo_id>')
def get_photo(photo_id: int) -> Response:
    return make_response(jsonify(photo_controller.find_by_id(photo_id)), HTTPStatus.OK)

@photo_bp.put('/<int:photo_id>')
def update_photo(photo_id: int) -> Response:
    content = request.get_json()
    photo = Photo.create_from_dto(content)
    photo_controller.update(photo_id, photo)
    return make_response("Photo updated", HTTPStatus.OK)

@photo_bp.patch('/<int:photo_id>')
def patch_photo(photo_id: int) -> Response:
    content = request.get_json()
    photo_controller.patch(photo_id, content)
    return make_response("Photo updated", HTTPStatus.OK)

@photo_bp.delete('/<int:photo_id>')
def delete_photo(photo_id: int) -> Response:
    photo_controller.delete(photo_id)
    return make_response("Photo deleted", HTTPStatus.OK)
