from sqlalchemy import Column, ForeignKey, String, DateTime

from cyber_components.db.models.product import Product


class RegionalInfo(Product):
    __tablename__ = "regional_info"

    id = Column(ForeignKey("product.id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "regional_info",
    }

    system_locale = Column(String)
    input_locale = Column(String)
    time_zone = Column(String)
