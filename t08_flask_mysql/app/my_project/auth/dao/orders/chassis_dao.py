from sqlalchemy import text
from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Chassis


class ChassisDAO(GeneralDAO):
    _domain_type = Chassis

    def insert_into_chassis(self, chassis_model: str, chassis_wheel_number: int):
        try:
            self.get_session().execute(text("CALL insert_into_chassis(:chassis_model, :chassis_wheel_number)"),
                                       {'chassis_model': chassis_model, 'chassis_wheel_number': chassis_wheel_number})
            self.get_session().commit()
        except Exception as e:
            print(f"Error: {e}")
