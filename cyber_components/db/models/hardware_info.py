from sqlalchemy import Column, ForeignKey, String, DateTime, Integer

from cyber_components.db.models.component import Component


class HardwareInfo(Component):
    __tablename__ = "hardware_info"

    id = Column(ForeignKey("component.id"), primary_key=True)
    parent_id = Column(ForeignKey("machine.id"))

    system_boot_time = Column(DateTime)
    system_manufacturer = Column(String)
    system_model = Column(String)
    system_type = Column(String)
    bois_version = Column(String)

    total_physical_memory = Column(Integer)
    available_physical_memory = Column(Integer)
    max_virtual_memory = Column(Integer)
    available_virtual_memory = Column(Integer)
    used_virtual_memory = Column(Integer)

    __mapper_args__ = {
        "polymorphic_identity": "hardware_info",
    }

    # processors

    def __repr__(self):
        return "<HardwareInfo>"
