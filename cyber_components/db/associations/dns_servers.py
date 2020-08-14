from sqlalchemy import Column, ForeignKey, PrimaryKeyConstraint

from cyber_components.db.connection import Connection


class DnsServers(Connection.Base):
    __tablename__ = "dns_servers"
    __table_args__ = (
        PrimaryKeyConstraint("server_id", "client_id"),
    )

    server_id = Column(ForeignKey("machine.id"))
    client_id = Column(ForeignKey("network_interface.id"))
