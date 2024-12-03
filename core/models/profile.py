from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from .mixins import UserRelationMixin


class Profile(UserRelationMixin, Base):
    _user_id_unique = True
    _user_back_populates = "profile"
    first_name: Mapped[str or None] = mapped_column(String(40), nullable=True)
    last_name: Mapped[str or None] = mapped_column(String(40), nullable=True)
    bio: Mapped[str or None] = mapped_column(nullable=True)
