"""Module to create table of albums"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.session import Base
from app.models.associations import association_table_albums_artists, association_table_albums_songs


class Album(Base):
    """Music Albums table"""

    __tablename__ = "albums"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, unique=True, nullable=False)
    icon_path = Column(String, nullable=True)

    artists = relationship("Artist", secondary=association_table_albums_artists, back_populates="albums")
    songs = relationship("Song", secondary=association_table_albums_songs, back_populates="albums")
