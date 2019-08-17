from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

from cyber_components.db.models.component import Component


class Network(Component):
    __tablename__ = "network"

    id = Column(ForeignKey("component.id"), primary_key=True)

    subnets = relationship(
        "Subnet",
        foreign_keys="Subnet.parent_id",
        backref="parent",
    )

    __mapper_args__ = {
        "polymorphic_identity": "network",
    }
