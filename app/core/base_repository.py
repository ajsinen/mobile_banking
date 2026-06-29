from app.core.database import get_pool


class BaseRepository:

    @property
    def pool(self):
        return get_pool()