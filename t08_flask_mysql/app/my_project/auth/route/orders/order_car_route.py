from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import order_car_controller
from t08_flask_mysql.app.my_project.auth.domain import OrderCar

order_car_bp = Blueprint('order_cars', __name__, url_prefix='/order_cars')

@order_car_bp.get('')
def get_all_order_cars() -> Response:
    return make_response(jsonify(order_car_controller.find_all()), HTTPStatus.OK)

@order_car_bp.post('')
def create_order_car() -> Response:
    content = request.get_json()
    order_car = OrderCar.create_from_dto(content)
    order_car_controller.create(order_car)
    return make_response(jsonify(order_car.put_into_dto()), HTTPStatus.CREATED)

@order_car_bp.get('/<int:order_id>/<int:car_id>')
def get_order_car(order_id: int, car_id: int) -> Response:
    return make_response(jsonify(order_car_controller.find_by_ids(order_id, car_id)), HTTPStatus.OK)

@order_car_bp.put('/<int:order_id>/<int:car_id>')
def update_order_car(order_id: int, car_id: int) -> Response:
    content = request.get_json()
    order_car = OrderCar.create_from_dto(content)
    order_car_controller.update(order_id, car_id, order_car)
    return make_response("OrderCar updated", HTTPStatus.OK)

@order_car_bp.patch('/<int:order_id>/<int:car_id>')
def patch_order_car(order_id: int, car_id: int) -> Response:
    content = request.get_json()
    order_car_controller.patch(order_id, car_id, content)
    return make_response("OrderCar updated", HTTPStatus.OK)

@order_car_bp.delete('/<int:order_id>/<int:car_id>')
def delete_order_car(order_id: int, car_id: int) -> Response:
    order_car_controller.delete(order_id, car_id)
    return make_response("OrderCar deleted", HTTPStatus.OK)

@order_car_bp.get('/<int:order_id>/cars')
def find_cars_by_order_id(order_id: int):
    return make_response(jsonify(order_car_controller.find_cars_by_order_id(order_id)), HTTPStatus.OK)

@order_car_bp.get('/<int:car_id>/orders')
def find_orders_by_car_id(car_id: int):
    return make_response(jsonify(order_car_controller.find_orders_by_car_id(car_id)), HTTPStatus.OK)
