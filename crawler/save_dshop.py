# save_dshop.py

from db.db import SessionLocal
from models.dshop import Dshop

dshop_data = []

def save_dshop_record(data: dict):
    global dshop_data
    dshop_data.append(data)

    if len(dshop_data) < 100:
        return

    session = SessionLocal()
    try:
        for d in dshop_data:
            # すでにindexが存在するか確認
            existing = session.query(Dshop).filter(Dshop.index == d["index"]).first()

            if existing:
                # 上書き（UPDATE）
                for key, value in d.items():
                    setattr(existing, key, value)
            else:
                # 新規追加（INSERT）
                new_record = Dshop(**d)
                session.add(new_record)

        session.commit()

    except Exception as e:
        session.rollback()
        raise e

    finally:
        session.close()
        dshop_data.clear()  # バッファをクリア


def save_dshop_record_finally():
    global dshop_data

    session = SessionLocal()
    try:
        for d in dshop_data:
            # すでにindexが存在するか確認
            existing = session.query(Dshop).filter(Dshop.index == d["index"]).first()

            if existing:
                # 上書き（UPDATE）
                for key, value in d.items():
                    setattr(existing, key, value)
            else:
                # 新規追加（INSERT）
                new_record = Dshop(**d)
                session.add(new_record)

        session.commit()

    except Exception as e:
        session.rollback()
        raise e

    finally:
        session.close()
        dshop_data.clear()  # バッファをクリア
