"""Module to create table of songs"""
from sqlalchemy import (
    ARRAY,
    DECIMAL,
    JSON,
    Boolean,
    Column,
    Date,
    ForeignKey,
    Integer,
    Interval,
    SmallInteger,
    String,
    func,
)
from sqlalchemy.orm import relationship

from app.db.session import Base
from app.models.associations import (
    association_table_albums_songs,
    association_table_songs_artists,
    association_table_songs_genres,
)
from app.utils.utils import generate_code


class Song(Base):
    """Songs table"""

    __tablename__ = "songs"

    id = Column(Integer, primary_key=True, nullable=False)
    artist = Column(String, nullable=True)
    album = Column(String, nullable=True)
    albumartist = Column(String, nullable=True)
    composer = Column(String, nullable=True)
    genre = Column(String, nullable=True)
    disc = Column(String, nullable=True)
    title = Column(String, nullable=True)
    comment = Column(String, nullable=True)
    year = Column(Date, nullable=True)
    disc_total = Column(String, nullable=True)
    duration = Column(Interval, nullable=True)
    filesize = Column(Integer, nullable=True)
    audio_offset = Column(Integer, nullable=True)
    bitrate = Column(DECIMAL, nullable=True)
    channels = Column(SmallInteger, nullable=True)
    samplerate = Column(Integer, nullable=True)
    bitdepth = Column(Integer, nullable=True)
    track = Column(String, nullable=True)
    track_total = Column(String, nullable=True)
    is_blocked = Column(Boolean, default=False, nullable=True)
    file_path = Column(String, default="", nullable=False)
    picture_path = Column(String, nullable=True)
    extra = Column(ARRAY(JSON), nullable=True)
    code_id = Column(String, nullable=False, default=generate_code, unique=True)
    source = Column(Integer, ForeignKey("songs_sources.id"), nullable=True, unique=False)

    blocked = relationship("BlockedSong", uselist=False, back_populates="song")
    song_source = relationship("SongSource", back_populates="song")
    artists = relationship("Artist", secondary=association_table_songs_artists, back_populates="songs")
    albums = relationship("Album", secondary=association_table_albums_songs, back_populates="songs")
    genres = relationship("Genre", secondary=association_table_songs_genres, back_populates="songs")


class BlockedSong(Base):
    """Class for blocked songs"""

    __tablename__ = "blocked_songs"

    id = Column(Integer, primary_key=True, nullable=False)
    song_id = Column(Integer, ForeignKey("songs.id"), nullable=False, unique=True)
    block_date = Column(Date, server_default=func.current_date(), nullable=False)
    block_reason = Column(String, nullable=False)
    blocked_by = Column(Integer, nullable=False)

    song = relationship("Song", back_populates="blocked")
