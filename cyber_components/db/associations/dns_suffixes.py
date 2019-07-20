from sqlalchemy import Column, ForeignKey, PrimaryKeyConstraint

from cyber_components.db.connection import Base


class DnsSuffixes(Base):
    __tablename__ = "dns_suffixes"
    __table_args__ = (
        PrimaryKeyConstraint("network_info_id", "suffix_id"),
    )

    network_info_id = Column(ForeignKey("network_info.id"))
    suffix_id = Column(ForeignKey("dns_suffix.id"))
