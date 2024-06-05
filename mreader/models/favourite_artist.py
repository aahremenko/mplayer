"""Module to create FavouriteArtist model"""
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.db.session import Base


class FavouriteArtist(Base):

    """Table for storing users favourites artists"""

    __tablename__ = "favourite_artists"

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, nullable=False)
    artist_id = Column(Integer, ForeignKey("artists.id"), nullable=False)

    artist = relationship("Artist", back_populates="favourite_artists")
