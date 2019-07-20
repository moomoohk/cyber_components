from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

from cyber_components.db import Target


class DnsServer(Target):
    __tablename__ = "dns_server"
    __mapper_args__ = {
        "polymorphic_identity": "dns_server",
    }

    id = Column(ForeignKey("target.id"), primary_key=True)

    clients = relationship(
        "NetworkInterface",
        secondary="dns_servers",
    )
