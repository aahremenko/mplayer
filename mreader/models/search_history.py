from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, UniqueConstraint

from app.db.session import Base


class SearchHistory(Base):
    """Search history table"""

    __tablename__ = "search_history"

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, nullable=False)
    search_text = Column(String, nullable=False)
    add_date = Column(DateTime, default=datetime.now)

    __table_args__ = (UniqueConstraint("user_id", "search_text", name="user_id_search_text_uс"),)
