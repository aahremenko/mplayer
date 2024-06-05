from sqlalchemy import Column, ForeignKey, Integer, Table, UniqueConstraint

from app.db.session import Base

association_table_songs_artists = Table(
    "songs_artists_association",
    Base.metadata,
    Column("song_id", Integer, ForeignKey("songs.id")),
    Column("artist_id", Integer, ForeignKey("artists.id")),
    UniqueConstraint("song_id", "artist_id", name="unique_song_artist_pair"),
)


association_table_albums_artists = Table(
    "album_artist_association",
    Base.metadata,
    Column("album_id", Integer, ForeignKey("albums.id")),
    Column("artist_id", Integer, ForeignKey("artists.id")),
    UniqueConstraint("album_id", "artist_id", name="unique_album_artist_pair"),
)


association_table_albums_songs = Table(
    "albums_songs_association",
    Base.metadata,
    Column("album_id", Integer, ForeignKey("albums.id")),
    Column("song_id", Integer, ForeignKey("songs.id")),
    UniqueConstraint("album_id", "song_id", name="unique_album_song_pair"),
)


association_table_songs_genres = Table(
    "songs_genres_association",
    Base.metadata,
    Column("song_id", Integer, ForeignKey("songs.id")),
    Column("genre_id", Integer, ForeignKey("genres.id")),
    UniqueConstraint("song_id", "genre_id", name="unique_song_genre_pair"),
)
