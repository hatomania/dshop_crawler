# made by ChatGPT

from db.db import SessionLocal
from models.dshop import Dshop
from sqlalchemy import func

class DShopData:
    _instance = None  # シングルトン用インスタンス保持

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.data_list = []
        return cls._instance

    def push(self, data: dict):
        d = {
            **data,
            "shop_name": None,
            "reception_time": None,
            "holidays": None,
            "address": None,
            "delivery_person": None,
            "note": None,
        }
        if "etags" not in d:
            d["etags"] = None
        self.data_list.append(data)

    @staticmethod
    def get_max_index():
        session = SessionLocal()
        try:
            max_index = session.query(func.max(Dshop.index)).scalar()
            #return max_index or -1
            return -1 if max_index is None else max_index
        finally:
            session.close()

    def flush(self):
        session = SessionLocal()
        try:
            for d in self.data_list:
                # indexが既に存在するか確認
                existing = session.query(Dshop).filter(Dshop.index == d["index"]).first()
                if existing:
                    for key, value in d.items():
                        setattr(existing, key, value)
                else:
                    new_record = Dshop(**d)
                    session.add(new_record)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
            self.data_list.clear()

    # コンテキストマネージャとしての対応
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.flush()
