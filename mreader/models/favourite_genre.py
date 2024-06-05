"""Module to create FavouriteGenre model"""
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.db.session import Base


class FavouriteGenre(Base):
    """Table to store users favourites genres"""

    __tablename__ = "favourite_genres"

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, nullable=False)
    genre_id = Column(Integer, ForeignKey("genres.id"), nullable=False)

    genre = relationship("Genre", back_populates="favourites")
