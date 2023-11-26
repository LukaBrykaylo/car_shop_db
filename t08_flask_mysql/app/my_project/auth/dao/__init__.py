# my_project/__init__.py

from .orders.client_dao import ClientDAO
from .orders.body_dao import BodyDAO
from .orders.chassis_dao import ChassisDAO
from .orders.drive_dao import DriveDAO
from .orders.engine_dao import EngineDAO
from .orders.model_dao import ModelDAO
from .orders.photo_dao import PhotoDAO
from .orders.car_dao import CarDAO
from .orders.city_dao import CityDAO
from .orders.comment_dao import CommentDAO
from .orders.shop_dao import ShopDAO
from .orders.order_dao import OrderDAO
from .orders.order_car_dao import OrderCarDAO
from .orders.test_drive_dao import TestDriveDAO

client_dao = ClientDAO()
body_dao = BodyDAO()
chassis_dao = ChassisDAO()
drive_dao = DriveDAO()
engine_dao = EngineDAO()
model_dao = ModelDAO()
photo_dao = PhotoDAO()
car_dao = CarDAO()
city_dao = CityDAO()
comment_dao = CommentDAO()
shop_dao = ShopDAO()
order_dao = OrderDAO()
order_car_dao = OrderCarDAO()
test_drive_dao = TestDriveDAO()
