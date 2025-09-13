# On-Chain Portfolio Analytics Backend

A flexible backend system for analyzing on-chain portfolio data with support for multiple database types.

> 📖 **For detailed installation and setup instructions, see [INSTALL.md](INSTALL.md)**

## Features

- **Multi-Database Support**: PostgreSQL, SQLite, and DuckDB
- **Flexible Configuration**: Environment-based configuration with pydantic-settings
- **SQLAlchemy ORM**: Full database abstraction and modeling
- **FastAPI Ready**: Built-in FastAPI integration support
- **Async Support**: Full async database operations

## Installation

For detailed installation instructions, see [INSTALL.md](INSTALL.md).

**Quick Start:**
```bash
# Clone and install with SQLite support (recommended for development)
git clone <repository-url>
cd on-chain-portfolio-analytics/backend
uv sync --extra sqlite
```

## Configuration

Create a `.env` file based on `env.example`. See [INSTALL.md](INSTALL.md) for detailed configuration examples.

**Key Environment Variables:**
- `DB_TYPE`: Choose `sqlite`, `duckdb`, or `postgresql`
- `DB_SQLITE_PATH`: Path for SQLite database file
- `DB_DUCKDB_PATH`: Path for DuckDB database file  
- `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`: PostgreSQL connection details
- `DB_ECHO`: Enable SQL query logging (useful for development)

## Usage

### Basic Database Operations

```python
from database import db_model, session

# Create tables
session.create_tables()

# Use the database
with session.db_manager.get_session_context() as db_session:
    # Create a wallet
    wallet = db_model.Wallet(
        address="0x1234...",
        label="My Wallet"
    )
    db_session.add(wallet)
    # Session automatically commits and closes
```

### FastAPI Integration

```python
from fastapi import FastAPI, Depends
from database import session, db_model
from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/wallets/")
def get_wallets(db: Session = Depends(session.get_db)):
    return db.query(db_model.Wallet).all()

@app.post("/wallets/")
def create_wallet(address: str, label: str, db: Session = Depends(session.get_db)):
    wallet = db_model.Wallet(address=address, label=label)
    db.add(wallet)
    db.commit()
    db.refresh(wallet)
    return wallet
```

### Async Operations

```python
from database import session, db_model
from sqlalchemy.ext.asyncio import AsyncSession

@app.get("/wallets/async")
async def get_wallets_async(db: AsyncSession = Depends(session.get_async_db)):
    result = await db.execute(select(db_model.Wallet))
    wallets = result.scalars().all()
    return wallets
```

## Database Initialization

### Initialize Database Schema

```bash
# Initialize with default configuration
python database/init_db.py

# Force recreate all tables (WARNING: deletes all data)
python database/init_db.py --force-recreate

# Drop all tables without recreating
python database/init_db.py --drop-only
```

### Programmatic Initialization

```python
from database import session

# Create all tables
session.create_tables()

# Drop all tables
session.drop_tables()
```

## Project Structure

```
backend/
├── database/
│   ├── __init__.py          # Main package exports
│   ├── config.py            # Database configuration
│   ├── db_model.py          # SQLAlchemy models
│   ├── session.py           # Database session management
│   ├── init_db.py           # Database initialization script
│   ├── config_examples.py   # Configuration examples
│   └── usage_examples.py    # Usage examples
├── main.py                  # FastAPI application entry point
├── pyproject.toml           # Project configuration
├── env.example              # Environment variables template
└── README.md                # This file
```

## Development

See [INSTALL.md](INSTALL.md) for dependency management and testing instructions.

**Quick Commands:**
```bash
# Install all database drivers for development
uv sync --extra all-databases

# Run tests
python -m pytest
```

## Database Compatibility

| Feature | SQLite | DuckDB | PostgreSQL |
|---------|--------|--------|------------|
| **CRUD Operations** | ✅ | ✅ | ✅ |
| **Foreign Keys** | ✅ | ✅ | ✅ |
| **Indexes** | ✅ | ✅ | ✅ |
| **Async Support** | ✅ | ⚠️ | ✅ |
| **Connection Pooling** | ❌ | ❌ | ✅ |
| **File-based** | ✅ | ✅ | ❌ |
| **Production Ready** | ❌ | ⚠️ | ✅ |

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

[Add your license here]
