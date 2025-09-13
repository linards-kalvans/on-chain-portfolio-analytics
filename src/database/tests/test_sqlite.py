import pytest
import os
from .. import Wallets, Transactions, TokenBalances

def test_sqlite_database_creation(sqlite_database):
    assert sqlite_database is not None
    assert os.path.exists(sqlite_database)
    assert os.path.getsize(sqlite_database) > 0
    assert sqlite_database.endswith(".sqlite")

def test_sqlite_basic_operations(sqlite_database, db_session, mock_database):
    # mock_database(db_session)
    print(db_session.query(Wallets).all())
    assert db_session.query(Wallets).count() == 1
    assert db_session.query(Transactions).count() == 1
    assert db_session.query(TokenBalances).count() == 1