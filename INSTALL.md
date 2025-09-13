# Installation Guide

This guide explains how to install the On-Chain Portfolio Analytics Backend with different database options.

> 📖 **For project overview, features, and usage examples, see [README.md](README.md)**

## Prerequisites

- Python 3.13 or higher
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

## Quick Start

### 1. Clone the Repository

```bash
git clone <repository-url>
cd on-chain-portfolio-analytics/backend
```

### 2. Choose Your Database Setup

#### Option A: SQLite (Recommended for Development)
```bash
uv sync --extra sqlite
```

#### Option B: DuckDB (Great for Analytics)
```bash
uv sync --extra duckdb
```

#### Option C: PostgreSQL (Production Ready)
```bash
uv sync --extra postgresql
```

#### Option D: All Database Types
```bash
uv sync --extra all-databases
```

## Detailed Installation

### Using uv (Recommended)

```bash
# Basic installation (no database drivers)
uv sync

# With specific database support
uv sync --extra sqlite      # SQLite only
uv sync --extra duckdb      # DuckDB only  
uv sync --extra postgresql  # PostgreSQL only
uv sync --extra all-databases  # All databases
```

### Using pip

```bash
# Basic installation (no database drivers)
pip install -e .

# With specific database support
pip install -e ".[sqlite]"      # SQLite only
pip install -e ".[duckdb]"      # DuckDB only
pip install -e ".[postgresql]"  # PostgreSQL only
pip install -e ".[all-databases]"  # All databases
```

## Database Driver Details

### SQLite (`[sqlite]`)
- **Driver**: `aiosqlite`
- **Use Case**: Local development, testing, prototyping
- **Pros**: No setup required, file-based, portable
- **Cons**: Limited concurrent access, no advanced features

### DuckDB (`[duckdb]`)
- **Drivers**: `duckdb`, `duckdb-engine`
- **Use Case**: Analytics workloads, data science, larger datasets
- **Pros**: Fast analytics queries, columnar storage, file-based
- **Cons**: Limited concurrent access, no native async support

### PostgreSQL (`[postgresql]`)
- **Driver**: `psycopg2-binary`
- **Use Case**: Production, staging, team development
- **Pros**: Full ACID compliance, advanced features, scalability
- **Cons**: Requires database server setup

## Environment Configuration

After installation, create a `.env` file:

```bash
# Copy the example
cp env.example .env

# Edit with your preferred database
nano .env
```

### Example Configurations

#### SQLite Development
```bash
DB_TYPE=sqlite
DB_SQLITE_PATH=dev_portfolio.db
DB_ECHO=true
```

#### DuckDB Analytics
```bash
DB_TYPE=duckdb
DB_DUCKDB_PATH=analytics.duckdb
DB_ECHO=false
```

#### PostgreSQL Production
```bash
DB_TYPE=postgresql
DB_HOST=localhost
DB_PORT=5432
DB_NAME=portfolio_analytics
DB_USER=postgres
DB_PASSWORD=your_password
DB_SCHEMA=public
DB_ECHO=false
DB_POOL_SIZE=20
```

## Verification

### Check Installation

```bash
# Verify database drivers are installed
uv pip list | grep -E "(psycopg2|aiosqlite|duckdb)"

# Test database connection
python database/init_db.py
```

### Test Database Operations

```python
from database import session, db_model

# Create tables
session.create_tables()

# Test basic operation
with session.db_manager.get_session_context() as db_session:
    wallet = db_model.Wallet(address="0x1234...", label="Test")
    db_session.add(wallet)
    print("Database connection successful!")
```

## Troubleshooting

### Common Issues

#### 1. "No module named 'psycopg2'"
```bash
# Install PostgreSQL support
uv sync --extra postgresql
```

#### 2. "No module named 'aiosqlite'"
```bash
# Install SQLite support
uv sync --extra sqlite
```

#### 3. "No module named 'duckdb'"
```bash
# Install DuckDB support
uv sync --extra duckdb
```

#### 4. Database Connection Errors
- Check your `.env` file configuration
- Verify database server is running (for PostgreSQL)
- Ensure file paths are correct (for SQLite/DuckDB)

### Getting Help

- Check the main [README.md](README.md) for detailed usage
- Review [database/config_examples.py](database/config_examples.py) for configuration examples
- Check [database/usage_examples.py](database/usage_examples.py) for usage patterns

## Next Steps

After successful installation:

1. **Configure Environment**: Set up your `.env` file
2. **Initialize Database**: Run `python database/init_db.py`
3. **Start Development**: Begin building your portfolio analytics application
4. **Check Examples**: Review the example files in the `database/` directory

## Support

If you encounter issues:

1. Check this installation guide
2. Review the main README
3. Check the example configuration files
4. Ensure all prerequisites are met
5. Verify your environment configuration
