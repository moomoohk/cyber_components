from sqlalchemy import Column, String, Integer

from cyber_components.db.connection import Connection


class Component(Connection.Base):
    __tablename__ = "component"

    id = Column(Integer, primary_key=True, autoincrement=True)
    _type = Column(String(50))

    __mapper_args__ = {
        "polymorphic_identity": "component",
        "polymorphic_on": _type,
    }
