from sqlalchemy import Column, ForeignKey, Integer, String, ARRAY, Numeric, TIMESTAMP
from sqlalchemy.orm import relationship

from database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    cards = relationship("Cards", back_populates="user")
    carts = relationship("Carts", back_populates="user")
    orders = relationship("Orders", back_populates="user")


class Categories(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    products = relationship("Products", back_populates="category")


class Types(Base):
    __tablename__ = "types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    carts = relationship("Carts", back_populates="type")
    order_details = relationship("OrderDetails", back_populates="type")


class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    main_image = Column(String)
    images = Column(ARRAY(String))
    description = Column(String)
    short_description = Column(String)
    price = Column(Numeric)
    weight = Column(String)
    dimensions = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("Categories", back_populates="products")
    carts = relationship("Carts", back_populates="product")
    order_details = relationship("OrderDetails", back_populates="product")


class CardFont(Base):
    __tablename__ = "card_font"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    attachments = Column(String)


class CardDecorations(Base):
    __tablename__ = "card_decorations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    attachments = Column(String)


class Cards(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    front = Column(String)
    back = Column(String)
    price = Column(Numeric)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("Users", back_populates="cards")
    carts = relationship("Carts", back_populates="card")
    order_details = relationship("OrderDetails", back_populates="card")


class Carts(Base):
    __tablename__ = "carts"

    id = Column(Integer, primary_key=True, index=True)
    type_id = Column(Integer, ForeignKey("types.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    card_id = Column(Integer, ForeignKey("cards.id"))
    created_time = Column(TIMESTAMP)

    type = relationship("Types", back_populates="carts")
    user = relationship("Users", back_populates="carts")
    product = relationship("Products", back_populates="carts")
    card = relationship("Cards", back_populates="carts")


class Orders(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Numeric)
    created_at = Column(TIMESTAMP)

    user = relationship("Users", back_populates="orders")
    order_details = relationship("OrderDetails", back_populates="order")


class OrderDetails(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    type_id = Column(Integer, ForeignKey("types.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    card_id = Column(Integer, ForeignKey("cards.id"))
    created_time = Column(TIMESTAMP)

    order = relationship("Orders", back_populates="order_details")
    type = relationship("Types", back_populates="order_details")
    product = relationship("Products", back_populates="order_details")
    card = relationship("Cards", back_populates="order_details")
