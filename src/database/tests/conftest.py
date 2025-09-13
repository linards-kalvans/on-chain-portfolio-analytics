import pytest
import os
import tempfile
import duckdb
from .. import setup_database, drop_database, SessionContext, Wallets, Transactions, TokenBalances
from datetime import datetime
import uuid

@pytest.fixture(scope="module")
def duckdb_database():
    with tempfile.TemporaryDirectory() as temp_dir:
        db_path = os.path.join(temp_dir, "test.duckdb")
        duckdb.connect(db_path)
        os.environ["DB_URL"] = f"duckdb:///{db_path}"
        setup_database()
        print(f"DuckDB database created at {db_path} at {datetime.now()}")
        yield db_path
        SessionContext.cache_clear()

@pytest.fixture(scope="module")
def sqlite_database():
    with tempfile.TemporaryDirectory() as temp_dir:
        db_path = os.path.join(temp_dir, "test.sqlite")
        os.environ["DB_URL"] = f"sqlite:///{db_path}"
        setup_database()
        print(f"SQLite database created at {db_path} at {datetime.now()}")
        yield db_path
        drop_database()
        SessionContext.cache_clear()

@pytest.fixture(scope="module")
def db_session():
    with SessionContext().get_db_session() as session:
        yield session

@pytest.fixture(scope="module")
def mock_database(db_session):
    wallet = Wallets(address=str(uuid.uuid4()), label="Test")
    db_session.add(wallet)
    print(f"Adding wallet to database: {os.getenv('DB_URL')} at {datetime.now()}")
    db_session.flush()
    db_session.add(Transactions(wallet_id=wallet.id, hash=str(uuid.uuid4()), from_address=str(uuid.uuid4()), to_address=str(uuid.uuid4()), value=1, gas_used=1, gas_price=1, block_number=1, block_timestamp=datetime.now(), chain_id=1))
    db_session.add(TokenBalances(wallet_id=wallet.id, token_address=str(uuid.uuid4()), token_symbol="Test", balance=1, usd_value=1, last_updated=datetime.now(), created_at=datetime.now()))
    db_session.commit()