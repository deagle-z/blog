from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, BigInteger, DATETIME, Table, MetaData

metaData = MetaData()

LoginAccount = Table(
    'user', metaData,
    Column("user_name", String),
    Column("password", String)
)
