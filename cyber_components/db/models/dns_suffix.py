from sqlalchemy import Column, ForeignKey, String

from cyber_components.db.models.product import Product


class DnsSuffix(Product):
    __tablename__ = "dns_suffix"

    id = Column(ForeignKey("product.id"), primary_key=True)

    suffix = Column(String(), unique=True)

    __mapper_args__ = {
        "polymorphic_identity": "dns_suffix",
    }

    def __repr__(self):
        return f"<DnsSuffix {self.suffix}>"
