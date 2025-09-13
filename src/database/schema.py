import sqlalchemy

Base = sqlalchemy.ext.declarative.declarative_base()

class Wallets(Base):
    __tablename__ = "wallets"
    id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.Sequence('wallets_id_seq'), primary_key=True)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    label = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False, default=sqlalchemy.func.now())

    def __repr__(self):
        return f"Wallets(id={self.id}, address={self.address}, label={self.label}, created_at={self.created_at})"

class Transactions(Base):
    __tablename__ = "transactions"
    id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.Sequence('transactions_id_seq'), primary_key=True)
    wallet_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('wallets.id'), nullable=False)
    hash = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    from_address = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    to_address = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    value = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    gas_used = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    gas_price = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    block_number = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    block_timestamp = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False)
    chain_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False, default=1)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False, default=sqlalchemy.func.now())
    __table_args__ = (sqlalchemy.UniqueConstraint('hash'),)

    def __repr__(self):
        return f"Transactions(id={self.id}, wallet_id={self.wallet_id}, hash={self.hash}, from_address={self.from_address}, to_address={self.to_address}, value={self.value}, gas_used={self.gas_used}, gas_price={self.gas_price}, block_number={self.block_number}, block_timestamp={self.block_timestamp}, chain_id={self.chain_id}, created_at={self.created_at})"
    

class TokenBalances(Base):
    __tablename__ = "token_balances"
    id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.Sequence('tokens_id_seq'), primary_key=True)
    wallet_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('wallets.id'), nullable=False)
    token_address = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    token_symbol = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    balance = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    usd_value = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    last_updated = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False, default=sqlalchemy.func.now())
    __table_args__ = (sqlalchemy.UniqueConstraint('token_address'),)

    def __repr__(self):
        return f"TokenBalances(id={self.id}, wallet_id={self.wallet_id}, token_address={self.token_address}, token_symbol={self.token_symbol}, balance={self.balance}, usd_value={self.usd_value}, last_updated={self.last_updated}, created_at={self.created_at})"