from typing import List

from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship

from cyber_components.db.models.product import Product


class FileSystemObject(Product):
    __tablename__ = "file_system_object"

    id = Column(ForeignKey("product.id"), primary_key=True)

    name = Column(String)

    files: List["File"] = relationship(
        "File",
        foreign_keys="File.parent_id",
        backref="parent",
    )
    folders: List["Folder"] = relationship(
        "Folder",
        foreign_keys="Folder.parent_id",
        backref="parent",
    )

    __mapper_args__ = {
        "polymorphic_identity": "file_system_object",
    }


class Drive(FileSystemObject):
    __tablename__ = "drive"

    id = Column(ForeignKey("file_system_object.id"), primary_key=True)
    parent_id = Column(ForeignKey("machine.id"))

    __mapper_args__ = {
        "polymorphic_identity": "drive",
    }

    def __init__(self, drive_letter=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.name = drive_letter or self.name

    @property
    def drive_letter(self):
        return self.name

    @drive_letter.setter
    def drive_letter(self, value):
        self.name = value

    def __repr__(self):
        return "<Drive{0}>".format(
            f" {self.drive_letter}:" if self.drive_letter is not None else "",
        )


class Folder(FileSystemObject):
    __tablename__ = "folder"

    id = Column(ForeignKey("file_system_object.id"), primary_key=True)
    parent_id = Column(ForeignKey("file_system_object.id"))

    __mapper_args__ = {
        "polymorphic_identity": "folder",
        "inherit_condition": id == FileSystemObject.id,
    }

    def __repr__(self):
        return "<Folder{0}>".format(
            f" {self.name}" if self.name is not None else "",
        )


class File(FileSystemObject):
    __tablename__ = "file"

    id = Column(ForeignKey("file_system_object.id"), primary_key=True)
    parent_id = Column(ForeignKey("file_system_object.id"))

    size = Column(Integer)

    __mapper_args__ = {
        "polymorphic_identity": "file",
        "inherit_condition": id == FileSystemObject.id,
    }

    def __repr__(self):
        return "<File{0}>".format(
            f" {self.name}" if self.name is not None else "",
        )
