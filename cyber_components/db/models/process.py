from sqlalchemy import Column, ForeignKey, Integer, String

from cyber_components.db.models.product import Product


class Process(Product):
    __tablename__ = "process"
    __mapper_args__ = {
        "polymorphic_identity": "process",
    }

    id = Column(ForeignKey("product.id"), primary_key=True)
    parent_id = Column(ForeignKey("session.id"))

    pid = Column(Integer)
    parent_pid = Column(Integer)
    name = Column(String)
    session_name = Column(String)

    def __repr__(self):
        return "<Process{0}{1}>".format(
            f" {self.name}" if self.name else "",
            f" ({self.pid})" if self.pid else "",
        )
