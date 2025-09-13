import sqlalchemy
from .settings import Settings
import contextlib
import functools

@functools.lru_cache(maxsize=None)
class SessionContext:
    def __init__(self):
        settings = Settings()
        engine = sqlalchemy.create_engine(settings.db_url)
        self.SessionLocal = sqlalchemy.orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

    @contextlib.contextmanager
    def get_db_session(self):
        session = self.SessionLocal()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
