from sqlalchemy import Column, String, Integer

from cyber_components.db.connection import Base


class Component(Base):
    __tablename__ = "component"

    id = Column(Integer, primary_key=True, autoincrement=True)
    _type = Column(String(50))

    __mapper_args__ = {
        "polymorphic_identity": "employee",
        "polymorphic_on": _type,
    }
