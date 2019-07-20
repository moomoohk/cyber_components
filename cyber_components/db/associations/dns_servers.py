from sqlalchemy import Column, ForeignKey, PrimaryKeyConstraint

from cyber_components.db.connection import Base


class DnsServers(Base):
    __tablename__ = "dns_servers"
    __table_args__ = (
        PrimaryKeyConstraint("server_id", "client_id"),
    )

    server_id = Column(ForeignKey("target.id"))
    client_id = Column(ForeignKey("network_interface.id"))