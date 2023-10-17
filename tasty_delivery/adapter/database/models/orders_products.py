from sqlalchemy import Table, Column, ForeignKey, MetaData
from sqlalchemy.dialects.postgresql import UUID

metadata = MetaData()
order_products = Table(
    'order_products',
    metadata,
    Column('order_id', UUID(as_uuid=True), ForeignKey('orders.id'), primary_key=True),
    Column('product_id', UUID(as_uuid=True), ForeignKey('products.id'), primary_key=True)
)