from enum import Enum
from typing import List, TYPE_CHECKING

from sqlalchemy import ForeignKey, Column, Boolean
from sqlalchemy import Enum as SqlEnum
from sqlalchemy.orm import relationship

from cyber_components.db.models.component import Component

if TYPE_CHECKING:
    from cyber_components.db import DnsSuffix, NetworkInterface, Component


class NodeType(Enum):
    BROADCAST = "Broadcast"
    PEER_TO_PEER = "Peer-Peer"
    MIXED = "Mixed"
    HYBRID = "Hybrid"
    UNKNOWN = "Unknown"


class NetworkInfo(Component):
    __tablename__ = "network_info"

    id = Column(ForeignKey("component.id"), primary_key=True)
    parent_id = Column(ForeignKey("machine.id"))

    primary_dns_suffix_id = Column(ForeignKey("dns_suffix.id"))
    node_type = Column(SqlEnum(NodeType))
    ip_routing_enabled = Column(Boolean())
    wins_proxy_enabled = Column(Boolean())

    interfaces: List["NetworkInterface"] = relationship(
        "NetworkInterface",
        foreign_keys="NetworkInterface.parent_id",
        backref="parent",
    )
    dns_suffix_search_list: List["DnsSuffix"] = relationship(
        "DnsSuffix",
        secondary="dns_suffixes",
    )

    __mapper_args__ = {
        "polymorphic_identity": "network_info",
    }

    def __repr__(self):
        return f"<NetworkInfo - {len(self.interfaces)} interfaces>"
