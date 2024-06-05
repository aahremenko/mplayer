"""Module to create Artist and ArtistGenre models"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.session import Base
from app.models.associations import association_table_albums_artists, association_table_songs_artists


class Artist(Base):
    """Table to store Artists"""

    __tablename__ = "artists"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False, unique=True)
    icon_path = Column(String, nullable=True)

    favourite_artists = relationship("FavouriteArtist", back_populates="artist")
    artists_genres = relationship("ArtistGenre", back_populates="artist")
    albums = relationship("Album", secondary=association_table_albums_artists, back_populates="artists")
    songs = relationship("Song", secondary=association_table_songs_artists, back_populates="artists")


class ArtistGenre(Base):
    """Table to store artists genres"""

    __tablename__ = "artists_genres"

    id = Column(Integer, primary_key=True, nullable=False)
    artist_id = Column(Integer, ForeignKey("artists.id"), nullable=False)
    genre_id = Column(Integer, ForeignKey("genres.id"), nullable=False)

    artist = relationship("Artist", back_populates="artists_genres")
    genre = relationship("Genre", back_populates="artists_genres")
