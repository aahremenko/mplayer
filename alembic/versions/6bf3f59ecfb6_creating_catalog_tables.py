"""Creating catalog tables

Revision ID: 33999ab35328
Revises: 
Create Date: 2023-12-10 23:24:19.222353

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6bf3f59ecfb6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('albums',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('icon_path', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('artists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('icon_path', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('genres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('search_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('search_text', sa.String(), nullable=False),
    sa.Column('add_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id', 'search_text', name='user_id_search_text_uс')
    )
    op.create_table('songs_sources',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('company_name', sa.String(), nullable=False),
    sa.Column('comment', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('album_artist_association',
    sa.Column('album_id', sa.Integer(), nullable=True),
    sa.Column('artist_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['album_id'], ['albums.id'], ),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.id'], ),
    sa.UniqueConstraint('album_id', 'artist_id', name='unique_album_artist_pair')
    )
    op.create_table('artists_genres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.id'], ),
    sa.ForeignKeyConstraint(['genre_id'], ['genres.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favourite_artists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favourite_genres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['genre_id'], ['genres.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('songs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist', sa.String(), nullable=True),
    sa.Column('album', sa.String(), nullable=True),
    sa.Column('albumartist', sa.String(), nullable=True),
    sa.Column('composer', sa.String(), nullable=True),
    sa.Column('genre', sa.String(), nullable=True),
    sa.Column('disc', sa.String(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('year', sa.Date(), nullable=True),
    sa.Column('disc_total', sa.String(), nullable=True),
    sa.Column('duration', sa.Interval(), nullable=True),
    sa.Column('filesize', sa.Integer(), nullable=True),
    sa.Column('audio_offset', sa.Integer(), nullable=True),
    sa.Column('bitrate', sa.DECIMAL(), nullable=True),
    sa.Column('channels', sa.SmallInteger(), nullable=True),
    sa.Column('samplerate', sa.Integer(), nullable=True),
    sa.Column('bitdepth', sa.Integer(), nullable=True),
    sa.Column('track', sa.String(), nullable=True),
    sa.Column('track_total', sa.String(), nullable=True),
    sa.Column('is_blocked', sa.Boolean(), nullable=True),
    sa.Column('file_path', sa.String(), nullable=False),
    sa.Column('picture_path', sa.String(), nullable=True),
    sa.Column('extra', sa.ARRAY(sa.JSON()), nullable=True),
    sa.Column('code_id', sa.String(), nullable=False),
    sa.Column('source', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['source'], ['songs_sources.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code_id')
    )
    op.create_table('albums_songs_association',
    sa.Column('album_id', sa.Integer(), nullable=True),
    sa.Column('song_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['album_id'], ['albums.id'], ),
    sa.ForeignKeyConstraint(['song_id'], ['songs.id'], ),
    sa.UniqueConstraint('album_id', 'song_id', name='unique_album_song_pair')
    )
    op.create_table('blocked_songs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('song_id', sa.Integer(), nullable=False),
    sa.Column('block_date', sa.Date(), server_default=sa.text('CURRENT_DATE'), nullable=False),
    sa.Column('block_reason', sa.String(), nullable=False),
    sa.Column('blocked_by', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['song_id'], ['songs.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('song_id')
    )
    op.create_table('songs_artists_association',
    sa.Column('song_id', sa.Integer(), nullable=True),
    sa.Column('artist_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.id'], ),
    sa.ForeignKeyConstraint(['song_id'], ['songs.id'], ),
    sa.UniqueConstraint('song_id', 'artist_id', name='unique_song_artist_pair')
    )
    op.create_table('songs_genres_association',
    sa.Column('song_id', sa.Integer(), nullable=True),
    sa.Column('genre_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['genre_id'], ['genres.id'], ),
    sa.ForeignKeyConstraint(['song_id'], ['songs.id'], ),
    sa.UniqueConstraint('song_id', 'genre_id', name='unique_song_genre_pair')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('songs_genres_association')
    op.drop_table('songs_artists_association')
    op.drop_table('blocked_songs')
    op.drop_table('albums_songs_association')
    op.drop_table('songs')
    op.drop_table('favourite_genres')
    op.drop_table('favourite_artists')
    op.drop_table('artists_genres')
    op.drop_table('album_artist_association')
    op.drop_table('songs_sources')
    op.drop_table('search_history')
    op.drop_table('genres')
    op.drop_table('artists')
    op.drop_table('albums')
    # ### end Alembic commands ###
