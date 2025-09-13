import pytest
import os
from .. import Wallets, Transactions, TokenBalances
# from .utils import mock_database

def test_duckdb_database_creation(duckdb_database):
    assert duckdb_database is not None
    assert os.path.exists(duckdb_database)
    assert os.path.getsize(duckdb_database) > 0
    assert duckdb_database.endswith(".duckdb")

def test_duckdb_basic_operations(duckdb_database, db_session, mock_database):
    # mock_database(db_session)
    print(db_session.query(Wallets).all())
    assert db_session.query(Wallets).count() == 1
    assert db_session.query(Transactions).count() == 1
    assert db_session.query(TokenBalances).count() == 1
    # assert False