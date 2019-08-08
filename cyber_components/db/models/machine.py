from typing import List

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from cyber_components.db.models.file_system import Drive
from cyber_components.db.models.os_info import OsInfo
from cyber_components.db.models.hardware_info import HardwareInfo
from cyber_components.db.models.network_info import NetworkInfo
from cyber_components.db.models.product import Product
from cyber_components.db.models.session import Session


class Machine(Product):
    __tablename__ = "machine"

    id = Column(ForeignKey("product.id"), primary_key=True)

    hostname = Column(String)

    network_info: NetworkInfo = relationship(
        "NetworkInfo",
        foreign_keys="NetworkInfo.parent_id",
        backref="parent",
        uselist=False,
    )
    sessions: List[Session] = relationship(
        "Session",
        foreign_keys="Session.parent_id",
        backref="parent",
    )
    os_info: OsInfo = relationship(
        "OsInfo",
        foreign_keys="OsInfo.parent_id",
        backref="parent",
        uselist=False,
    )
    hardware_info: HardwareInfo = relationship(
        "HardwareInfo",
        foreign_keys="HardwareInfo.parent_id",
        backref="parent",
        uselist=False,
    )
    drives: List[Drive] = relationship(
        "Drive",
        foreign_keys="Drive.parent_id",
        backref="parent",
    )

    __mapper_args__ = {
        "polymorphic_identity": "machine",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.network_info = NetworkInfo()
        self.os_info = OsInfo()
        self.hardware_info = HardwareInfo()

    def __repr__(self):
        return "<Machine{0}>".format(
            f" {self.hostname}" if self.hostname else ""
        )

    def get_session(self, number: int) -> Session:
        for session in self.sessions:
            if session.number == number:
                return session
