from typing import List

from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship

from cyber_components.db.models.component import Component


class FileSystemObject(Component):
    __tablename__ = "file_system_object"

    id = Column(ForeignKey("component.id"), primary_key=True)

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

    letter = Column(String)

    __mapper_args__ = {
        "polymorphic_identity": "drive",
    }

    @property
    def path(self):
        return f"{self.letter}:"

    def __repr__(self):
        return "<Drive{0}>".format(
            f" {self.letter}:" if self.letter is not None else "",
        )


class SubItem(FileSystemObject):
    __tablename__ = "fs_subitem"

    id = Column(ForeignKey("file_system_object.id"), primary_key=True)
    parent_id = Column(ForeignKey("file_system_object.id"))

    name = Column(String)

    __mapper_args__ = {
        "polymorphic_identity": "fs_subitem",
        "inherit_condition": id == FileSystemObject.id,
    }

    @property
    def path(self):
        return f"{self.parent.path}\\{self.name}"


class Folder(SubItem):
    __tablename__ = "folder"

    id = Column(ForeignKey("fs_subitem.id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "folder",
    }

    def __repr__(self):
        return "<Folder{0}>".format(
            f" {self.name}" if self.name is not None else "",
        )


class File(SubItem):
    __tablename__ = "file"

    id = Column(ForeignKey("fs_subitem.id"), primary_key=True)

    size = Column(Integer)

    __mapper_args__ = {
        "polymorphic_identity": "file",
    }

    def __repr__(self):
        return "<File{0}>".format(
            f" {self.name}" if self.name is not None else "",
        )
