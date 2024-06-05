"""Module to create table of music genres"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.session import Base
from app.models.associations import association_table_songs_genres


class Genre(Base):
    """Music Genre table"""

    __tablename__ = "genres"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, unique=True, nullable=False)

    favourites = relationship("FavouriteGenre", back_populates="genre")
    artists_genres = relationship("ArtistGenre", back_populates="genre")
    songs = relationship("Song", secondary=association_table_songs_genres, back_populates="genres")
