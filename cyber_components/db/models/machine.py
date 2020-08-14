from typing import List, Optional

from cyber_components.db.connection import Connection
from cyber_components.db.models.component import Component
from cyber_components.db.models.file_system import Drive
from cyber_components.db.models.hardware_info import HardwareInfo
from cyber_components.db.models.network_info import NetworkInfo
from cyber_components.db.models.os_info import OsInfo
from cyber_components.db.models.process import Process
from cyber_components.db.models.session import Session
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class Machine(Component):
    __tablename__ = "machine"

    id = Column(ForeignKey("component.id"), primary_key=True)

    hostname = Column(String)

    sessions: List[Session] = relationship(
        Session,
        foreign_keys="Session.parent_id",
        backref="parent",
    )
    processes: List[Process] = relationship(
        "Process",
        foreign_keys="Process.parent_id",
        backref="parent",
    )
    drives: List[Drive] = relationship(
        Drive,
        foreign_keys="Drive.parent_id",
        backref="parent",
    )

    network_info: NetworkInfo = relationship(
        NetworkInfo,
        foreign_keys="NetworkInfo.parent_id",
        backref="parent",
        uselist=False,
    )
    os_info: OsInfo = relationship(
        OsInfo,
        foreign_keys="OsInfo.parent_id",
        backref="parent",
        uselist=False,
    )
    hardware_info: HardwareInfo = relationship(
        HardwareInfo,
        foreign_keys="HardwareInfo.parent_id",
        backref="parent",
        uselist=False,
    )

    __mapper_args__ = {
        "polymorphic_identity": "machine",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.network_info = NetworkInfo()
        self.os_info = OsInfo()
        self.hardware_info = HardwareInfo()

    def __repr__(self):
        return "<Machine{0}>".format(
            f" {self.hostname}" if self.hostname else ""
        )

    def get_session(self, number: int) -> Optional[Session]:
        return Connection.session.query(Session).filter_by(number=number, parent_id=self.id).one_or_none()

    def get_process_by_pid(self, pid: int) -> Optional[Process]:
        from cyber_components.db import Process

        for session in self.sessions:
            process = Connection.session.query(Process).filter_by(pid=pid, parent_id=session.id).one_or_none()

            if process is not None:
                return process

        return None

    def get_process_by_name(self, name: str) -> Optional[Process]:
        for process in self.processes:
            if process.name == name:
                return process

        return None
