from sqlalchemy import Column, ForeignKey, String, DateTime

from cyber_components.db.models.product import Product


class OsInfo(Product):
    __tablename__ = "os_info"

    id = Column(ForeignKey("product.id"), primary_key=True)
    parent_id = Column(ForeignKey("machine.id"))

    name = Column(String)
    version = Column(String)
    manufacturer = Column(String)
    configuration = Column(String)
    build_type = Column(String)
    registered_owner = Column(String)
    registered_organization = Column(String)
    product_id = Column(String)
    original_install_date = Column(DateTime)

    __mapper_args__ = {
        "polymorphic_identity": "os_info",
    }

    # hotfixes

    def __repr__(self):
        return "<OsInfo{0}>".format(
            self.name if self.name is not None else ""
        )
