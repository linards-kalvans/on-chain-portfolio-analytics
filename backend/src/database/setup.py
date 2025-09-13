import sqlalchemy
import sqlalchemy_utils
from .settings import Settings
from .schema import Base


def setup_database():
    settings = Settings()
    # if not sqlalchemy_utils.database_exists(settings.db_url):
    #     sqlalchemy_utils.create_database(settings.db_url)
    print(f"Setting up database at {settings.db_url}")
    engine = sqlalchemy.create_engine(settings.db_url)
    Base.metadata.create_all(engine)

def drop_database():
    settings = Settings()
    if sqlalchemy_utils.database_exists(settings.db_url):
        sqlalchemy_utils.drop_database(settings.db_url)

if __name__ == "__main__":
    setup_database()