from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import order_controller
from t08_flask_mysql.app.my_project.auth.domain import Order
from t08_flask_mysql.app.my_project.auth.domain.orders.order import order_has_car

order_bp = Blueprint('orders', __name__, url_prefix='/orders')


@order_bp.get('')
def get_all_orders() -> Response:
    return make_response(jsonify(order_controller.find_all()), HTTPStatus.OK)


@order_bp.post('')
def create_order() -> Response:
    content = request.get_json()
    order = Order.create_from_dto(content)
    order_controller.create(order)
    return make_response(jsonify(order.put_into_dto()), HTTPStatus.CREATED)


@order_bp.get('/<int:order_id>')
def get_order(order_id: int) -> Response:
    return make_response(jsonify(order_controller.find_by_id(order_id)), HTTPStatus.OK)


@order_bp.put('/<int:order_id>')
def update_order(order_id: int) -> Response:
    content = request.get_json()
    order = Order.create_from_dto(content)
    order_controller.update(order_id, order)
    return make_response("Order updated", HTTPStatus.OK)


@order_bp.patch('/<int:order_id>')
def patch_order(order_id: int) -> Response:
    content = request.get_json()
    order_controller.patch(order_id, content)
    return make_response("Order updated", HTTPStatus.OK)


@order_bp.delete('/<int:order_id>')
def delete_order(order_id: int) -> Response:
    order_controller.delete(order_id)
    return make_response("Order deleted", HTTPStatus.OK)


@order_bp.get('/<int:order_id>/cars')
def get_all_orders_from_cars(order_id) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(order_controller.find_cars(order_id)), HTTPStatus.OK)


@order_bp.post('/<int:order_id>/order_car')
def add_car_to_order(order_id) -> Response:
    try:
        data = request.get_json()
        car_id = data.get('car_id')

        order_controller.add_car_to_order(order_id, car_id)

        return make_response(jsonify({"message": "Car added successfully"}), HTTPStatus.OK)

    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@order_bp.get('/<int:order_id>/cars')
def get_all_cars_from_order(order_id) -> Response:
    return make_response(jsonify(order_controller.find_cars(order_id)), HTTPStatus.OK)


@order_bp.patch('/<int:order_id>/remove_car')
def remove_car_from_order_id(order_id) -> Response:
    try:
        data = request.get_json()
        car_id = data.get('car_id')

        order_controller.remove_car_from_order_id(order_id, car_id)

        return make_response(jsonify({"message": "Car removed"}), HTTPStatus.OK)

    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)

@order_bp.post('/add_order_car')
def insert_into_order_car_with_checks() -> Response:
    content = request.get_json()

    order_id = content.get('order_id')
    car_length = content.get('car_length')
    car_width = content.get('car_width')
    car_engine_id = content.get('car_engine_id')
    car_body_id = content.get('car_body_id')
    car_body_type = content.get('car_body_type')
    car_chassis_id = content.get('car_chassis_id')
    car_drive_id = content.get('car_drive_id')
    car_photo_id = content.get('car_photo_id')
    car_model_id = content.get('car_model_id')

    if any(cont is None for cont in [order_id, car_length, car_width, car_engine_id,
                                     car_body_id, car_body_type, car_chassis_id, car_drive_id,
                                     car_photo_id, car_model_id]):
        return make_response('Bad Request', HTTPStatus.BAD_REQUEST)
    try:
        order_controller.insert_into_order_car_with_checks(order_id, car_length, car_width, car_engine_id,
                                     car_body_id, car_body_type, car_chassis_id, car_drive_id,
                                     car_photo_id, car_model_id)
        return make_response('Added', HTTPStatus.CREATED)
    except Exception as e:
        return make_response(f'Error: {str(e)}', HTTPStatus.INTERNAL_SERVER_ERROR)
