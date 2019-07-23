from enum import Enum
from typing import List

from sqlalchemy import Enum as SqlEnum
from sqlalchemy import ForeignKey, Column, Integer
from sqlalchemy.orm import relationship

from cyber_components.db.models.product import Product


class PortState(Enum):
    LISTENING = 0
    CLOSE_WAIT = 1
    ESTABLISHED = 2
    TIME_WAIT = 3


class Protocol(Enum):
    TCP = 0
    UDP = 1
    TCPv6 = 2
    UDPv6 = 3


class Port(Product):
    __tablename__ = "port"
    __mapper_args__ = {
        "polymorphic_identity": "port",
    }

    id = Column(ForeignKey("product.id"), primary_key=True)
    parent_id = Column(ForeignKey("network_interface.id"))

    protocol = Column(SqlEnum(Protocol))
    number = Column(Integer)
    state = Column(SqlEnum(PortState))
    pid = Column(ForeignKey("process.pid"))
    connected_to_id = Column(ForeignKey("port.id"))

    connections: List["Port"] = relationship(
        "Port",
        foreign_keys="Port.connected_to_id",
    )

    def __repr__(self):
        return "<Port{0}{1}{2}>".format(
            f" {self.number}" if self.number is not None else "",
            f" {self.protocol}" if self.protocol is not None else "",
            f" {self.state}" if self.state.name is not None else "",
        )
