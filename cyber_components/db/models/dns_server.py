from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

from cyber_components.db.models.machine import Machine


class DnsServer(Machine):
    __tablename__ = "dns_server"

    id = Column(ForeignKey("machine.id"), primary_key=True)

    clients = relationship(
        "NetworkInterface",
        secondary="dns_servers",
    )

    __mapper_args__ = {
        "polymorphic_identity": "dns_server",
    }
