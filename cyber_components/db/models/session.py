from typing import List

from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship

from cyber_components.db.models.component import Component

from cyber_components.db.models.process import Process


class Session(Component):
    __tablename__ = "session"

    id = Column(ForeignKey("component.id"), primary_key=True)
    parent_id = Column(ForeignKey("machine.id"))

    number = Column(Integer)
    name = Column(String)

    processes: List[Process] = relationship("Process", foreign_keys="Process.session_id", uselist=True, backref="session")

    __mapper_args__ = {
        "polymorphic_identity": "session",
    }

    def __repr__(self):
        return "<Session{0}{1}>".format(
            f" {self.number}" if self.number is not None else "",
            f" {self.name}" if self.name is not None else "",
        )
