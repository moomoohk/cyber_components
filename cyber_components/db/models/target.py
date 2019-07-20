from typing import List

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from cyber_components.db.models.network_info import NetworkInfo
from cyber_components.db.models.product import Product
from cyber_components.db.models.session import Session


class Target(Product):
    __tablename__ = "target"
    __mapper_args__ = {
        "polymorphic_identity": "target",
    }

    id = Column(ForeignKey("product.id"), primary_key=True)

    hostname = Column(String)

    network_info: NetworkInfo = relationship(
        "NetworkInfo",
        foreign_keys="NetworkInfo.parent_id",
        backref="parent",
        uselist=False,
    )
    sessions: List[Session] = relationship(
        "Session",
        foreign_keys="Session.parent_id",
        backref="parent",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.network_info = NetworkInfo()

    def __repr__(self):
        return "<Target{0}>".format(
            f" {self.hostname}" if self.hostname else ""
        )

    def get_session(self, number: int) -> Session:
        for session in self.sessions:
            if session.number == number:
                return session
