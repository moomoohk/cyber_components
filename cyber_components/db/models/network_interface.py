from enum import Enum
from typing import List, TYPE_CHECKING

from sqlalchemy import Enum as SqlEnum
from sqlalchemy import ForeignKey, Column, String, Boolean, Integer
from sqlalchemy.orm import relationship
from sqlalchemy_utils import IPAddressType

from cyber_components.db.models.port import Port
from cyber_components.db.models.component import Component
from cyber_components.db.connection import session

if TYPE_CHECKING:
    from cyber_components.db import DnsServer, DnsSuffix, Machine


class InterfaceType(Enum):
    WIRELESS_LAN = "Wireless LAN"
    ETHERNET = "Ethernet"
    TUNNEL = "Tunnel"


class NetworkInterface(Component):
    __tablename__ = "network_interface"

    id = Column(ForeignKey("component.id"), primary_key=True)
    parent_id = Column(ForeignKey("network_info.id"))

    type = Column(SqlEnum(InterfaceType))
    name = Column(String())
    disconnected = Column(Boolean(), default=False)
    dns_suffix_id = Column(ForeignKey("dns_suffix.id"))
    description = Column(String())
    mac = Column(String())  # TODO: MAC type
    dhcp_enabled = Column(Boolean())
    autoconfiguration_enabled = Column(Boolean())
    link_local_ipv6 = Column(IPAddressType())
    link_local_ipv6_preferred = Column(Boolean(), default=False)
    ipv4 = Column(IPAddressType())
    ipv4_preferred = Column(Boolean(), default=False)
    subnet_mask = Column(IPAddressType())
    lease_obtained = Column(String())  # TODO: Datetime
    lease_expires = Column(String())  # TODO: Datetime
    default_gateway_id = Column(ForeignKey("network_interface.id"))
    dhcp_server_id = Column(ForeignKey("network_interface.id"))
    dhcpv6_client_iaid = Column(Integer())
    dhcpv6_client_duid = Column(String())
    netbios_over_tcpip_enabled = Column(Boolean())

    dns_suffix: "DnsSuffix" = relationship(
        "DnsSuffix",
        foreign_keys="NetworkInterface.dns_suffix_id",
        uselist=False,
    )
    dns_servers: List["DnsServer"] = relationship(
        "DnsServer",
        secondary="dns_servers",
    )
    default_gateway: "Machine" = relationship(
        "NetworkInterface",
        foreign_keys="NetworkInterface.default_gateway_id",
        uselist=False,
    )
    dhcp_server: "Machine" = relationship(
        "NetworkInterface",
        foreign_keys="NetworkInterface.dhcp_server_id",
        uselist=False,
    )
    bound_ports: List["Port"] = relationship(
        "Port",
        foreign_keys="Port.parent_id",
        backref="parent"
    )

    __mapper_args__ = {
        "polymorphic_identity": "network_interface",
    }

    def __repr__(self):
        short_name = self.name

        if short_name is not None and self.name.startswith("isatap"):
            short_name = "isatap..."

        return "<{0}{1}{2}>".format(
            f"{self.type.value} Interface" if self.type is not None else "NetworkInterface",
            f" - {short_name}" if short_name is not None else "",
            f" ({self.ipv4})" if self.ipv4 is not None else "",
        )

    @staticmethod
    def get_interface_by_ip(ip: str):
        return session.query(NetworkInterface) \
            .filter(NetworkInterface.ipv4 == ip) \
            .one_or_none()
