from .orders.client_controller import ClientController
from .orders.body_controller import BodyController
from .orders.chassis_controller import ChassisController
from .orders.drive_controller import DriveController
from .orders.engine_controller import EngineController
from .orders.model_controller import ModelController
from .orders.photo_controller import PhotoController
from .orders.car_controller import CarController
from .orders.city_controller import CityController
from .orders.comment_controller import CommentController
from .orders.shop_controller import ShopController
from .orders.order_controller import OrderController
from .orders.order_car_controller import OrderCarController
from .orders.test_drive_controller import TestDriveController

client_controller = ClientController()
body_controller = BodyController()
chassis_controller = ChassisController()
drive_controller = DriveController()
engine_controller = EngineController()
model_controller = ModelController()
photo_controller = PhotoController()
car_controller = CarController()
city_controller = CityController()
comment_controller = CommentController()
shop_controller = ShopController()
order_controller = OrderController()
order_car_controller = OrderCarController()
test_drive_controller = TestDriveController()
