from ipaddress import IPv4Network as _IPv4Network
from typing import List

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship, composite

from cyber_components.db.models.component import Component
from cyber_components.db.models.machine import Machine
from cyber_components.db.models.network_interface import NetworkInterface


class IPv4Network(_IPv4Network):
    def __init__(self, address, mask=None):
        if mask is None:
            super().__init__(address)
        else:
            super().__init__((address, mask))

    def __composite_values__(self):
        return int(self.network_address), self.prefixlen, self.max_prefixlen


class Subnet(Component):
    __tablename__ = "subnet"

    id = Column(ForeignKey("component.id"), primary_key=True)
    parent_id = Column(ForeignKey("network.id"))

    start_address = Column(Integer())
    prefix_length = Column(Integer())
    max_prefix_length = Column(Integer())
    gateway_id = Column(ForeignKey("machine.id"))

    subnet = composite(IPv4Network, start_address, prefix_length, max_prefix_length)

    gateway = relationship(
        Machine,
        foreign_keys=gateway_id,
    )

    interfaces: List[NetworkInterface] = relationship(
        NetworkInterface,
        foreign_keys=start_address,
        primaryjoin='Subnet.start_address.op(">>")(Subnet.max_prefix_length - Subnet.prefix_length) == '
                    'remote(NetworkInterface._ipv4).op(">>")'
                    '(Subnet.max_prefix_length - remote(NetworkInterface.subnet_prefix_length))',
        backref="subnet",
        uselist=False,
    )

    __mapper_args__ = {
        "polymorphic_identity": "subnet",
    }

    def __init__(self, start_address, mask=None):
        if mask is None:
            super().__init__(subnet=IPv4Network(start_address))
        else:
            super().__init__(subnet=IPv4Network((start_address, mask)))

    def __repr__(self):
        return "<Subnet{0} - {1} interface{2}>".format(
            f" {self.subnet}" if self.subnet is not None else "",
            len(self.interfaces),
            "s" if len(self.interfaces) != 1 else "",
        )
