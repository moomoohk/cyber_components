from enum import Enum
from typing import List, TYPE_CHECKING

from sqlalchemy import Enum as SqlEnum
from sqlalchemy import ForeignKey, Column, String, Boolean, Integer
from sqlalchemy.orm import relationship
from sqlalchemy_utils import IPAddressType

from cyber_components.db.models.product import Product

if TYPE_CHECKING:
    from cyber_components.db import DnsServer, DnsSuffix, Target


class InterfaceType(Enum):
    WIRELESS_LAN = "Wireless LAN"
    ETHERNET = "Ethernet"
    TUNNEL = "Tunnel"


class NetworkInterface(Product):
    __tablename__ = "network_interface"
    __mapper_args__ = {
        "polymorphic_identity": "network_interface",
    }

    id = Column(ForeignKey("product.id"), primary_key=True)
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
    default_gateway: "Target" = relationship(
        "NetworkInterface",
        foreign_keys="NetworkInterface.default_gateway_id",
        uselist=False,
    )
    dhcp_server: "Target" = relationship(
        "NetworkInterface",
        foreign_keys="NetworkInterface.dhcp_server_id",
        uselist=False,
    )

    def __repr__(self):
        return "<NetworkInterface{0}>".format(
            f" {self.name}" if self.name is not None else ""
        )
