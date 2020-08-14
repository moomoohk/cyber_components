from sqlalchemy import Column, ForeignKey, Integer, String

from cyber_components.db.models.component import Component


class Process(Component):
    __tablename__ = "process"

    id = Column(ForeignKey("component.id"), primary_key=True)
    parent_id = Column(ForeignKey("machine.id"))

    pid = Column(Integer)
    parent_pid = Column(Integer)
    name = Column(String)
    session_id = Column(ForeignKey("session.id"))

    __mapper_args__ = {
        "polymorphic_identity": "process",
    }

    def __repr__(self):
        return "<Process{0}{1}>".format(
            f" {self.name}" if self.name else "",
            f" ({self.pid})" if self.pid else "",
        )
