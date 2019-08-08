from typing import List

from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship

from cyber_components.db.models.product import Product

from cyber_components.db.models.process import Process


class Session(Product):
    __tablename__ = "session"

    id = Column(ForeignKey("product.id"), primary_key=True)
    parent_id = Column(ForeignKey("machine.id"))

    number = Column(Integer)
    name = Column(String)

    __mapper_args__ = {
        "polymorphic_identity": "session",
    }

    processes: List[Process] = relationship(
        "Process",
        foreign_keys="Process.parent_id",
        backref="parent",
    )

    def __repr__(self):
        return "<Session{0}{1}>".format(
            f" {self.number}" if self.number is not None else "",
            f" {self.name}" if self.name is not None else "",
        )

    def get_process_by_ip(self, pid: int) -> Process:
        for process in self.processes:
            if process.pid == pid:
                return process

    def get_process_by_name(self, name: str) -> Process:
        for process in self.processes:
            if process.name == name:
                return process
