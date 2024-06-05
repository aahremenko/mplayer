from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.session import Base


class SongSource(Base):
    """Songs sources table"""

    __tablename__ = "songs_sources"

    id = Column(Integer, primary_key=True, nullable=False)
    company_name = Column(String, nullable=False)
    comment = Column(String, nullable=True)

    song = relationship("Song", back_populates="song_source")
