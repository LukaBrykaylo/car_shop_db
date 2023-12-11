from .orders.client_service import ClientService
from .orders.body_service import BodyService
from .orders.chassis_service import ChassisService
from .orders.drive_service import DriveService
from .orders.engine_service import EngineService
from .orders.model_service import ModelService
from .orders.photo_service import PhotoService
from .orders.car_service import CarService
from .orders.city_service import CityService
from .orders.comment_service import CommentService
from .orders.shop_service import ShopService
from .orders.order_service import OrderService
from .orders.order_car_service import OrderCarService
from .orders.test_drive_service import TestDriveService

client_service = ClientService()
body_service = BodyService()
chassis_service = ChassisService()
drive_service = DriveService()
engine_service = EngineService()
model_service = ModelService()
photo_service = PhotoService()
car_service = CarService()
city_service = CityService()
comment_service = CommentService()
shop_service = ShopService()
order_service = OrderService()
order_car_service = OrderCarService()
test_drive_service = TestDriveService()
