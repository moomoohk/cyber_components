from sqlalchemy import event
from sqlalchemy.orm import mapper

from cyber_components.db.connection import Base, session, engine
from cyber_components.db.connection import Session as _Session

from cyber_components.db.associations.dns_suffixes import DnsSuffixes
from cyber_components.db.associations.dns_servers import DnsServers
from cyber_components.db.connection import Base, session, engine
from cyber_components.db.models.dns_server import DnsServer
from cyber_components.db.models.dns_suffix import DnsSuffix
from cyber_components.db.models.network_info import NetworkInfo, NodeType
from cyber_components.db.models.network_interface import NetworkInterface, InterfaceType
from cyber_components.db.models.port import Port, PortState, Protocol
from cyber_components.db.models.process import Process
from cyber_components.db.models.component import Component
from cyber_components.db.models.session import Session
from cyber_components.db.models.machine import Machine
from cyber_components.db.models.os_info import OsInfo
from cyber_components.db.models.hardware_info import HardwareInfo
from cyber_components.db.models.regional_info import RegionalInfo
from cyber_components.db.models.file_system import Drive, File, Folder, FileSystemObject
from cyber_components.db.models.network import Network
from cyber_components.db.models.subnet import Subnet

# Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


@event.listens_for(mapper, "init")
def auto_add(target, args, kwargs):
    session.add(target)
