from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .orders.client_route import client_bp
    from .orders.body_route import body_bp
    from .orders.car_route import car_bp
    from .orders.chassis_route import chassis_bp
    from .orders.city_route import city_bp
    from .orders.comment_route import comment_bp
    from .orders.drive_route import drive_bp
    from .orders.engine_route import engine_bp
    from .orders.model_route import model_bp
    from .orders.photo_route import photo_bp
    from .orders.shop_route import shop_bp
    from .orders.order_route import order_bp
    from .orders.order_car_route import order_car_bp
    from .orders.test_drive_route import test_drive_bp

    app.register_blueprint(client_bp)
    app.register_blueprint(body_bp)
    app.register_blueprint(car_bp)
    app.register_blueprint(chassis_bp)
    app.register_blueprint(city_bp)
    app.register_blueprint(comment_bp)
    app.register_blueprint(drive_bp)
    app.register_blueprint(engine_bp)
    app.register_blueprint(model_bp)
    app.register_blueprint(photo_bp)
    app.register_blueprint(shop_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(order_car_bp)
    app.register_blueprint(test_drive_bp)
