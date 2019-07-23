from cyber_components.db.connection import Base, session, engine

from cyber_components.db.associations.dns_suffixes import DnsSuffixes
from cyber_components.db.associations.dns_servers import DnsServers
from cyber_components.db.connection import Base, session, engine
from cyber_components.db.models.dns_server import DnsServer
from cyber_components.db.models.dns_suffix import DnsSuffix
from cyber_components.db.models.network_info import NetworkInfo, NodeType
from cyber_components.db.models.network_interface import NetworkInterface, InterfaceType
from cyber_components.db.models.port import Port, PortState, Protocol
from cyber_components.db.models.process import Process
from cyber_components.db.models.product import Product
from cyber_components.db.models.session import Session
from cyber_components.db.models.target import Target

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


def get_target_by_ip(ip: str):
    target = session.query(NetworkInterface)\
        .filter(NetworkInterface.ipv4 == ip)\
        .one_or_none()

    if target is not None:
        return target.parent.parent
