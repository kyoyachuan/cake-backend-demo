from sqlalchemy.orm import Session

import models
import schemas


class Types:
    product = 1
    card = 2


def get_user(db: Session, id: int = None, username: str = None, email: str = None):
    db_user = db.query(models.Users)
    if id:
        db_user = db_user.filter(models.Users.id == id)
    elif username:
        db_user = db_user.filter(models.Users.username == username)
    elif email:
        db_user = db_user.filter(models.Users.email == email)
    else:
        raise Exception('No user id or username or email')
    return db_user.first()


def create_user(db: Session, user: schemas.RegisterForm):
    db_user = models.Users(
        username=user.username,
        email=user.email,
        password=user.password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_products(db: Session, skip: int = 0, limit: int = 100, category: str = None):
    if category:
        dbq = db.query(models.Products, models.Categories)
        dbq = dbq.filter(models.Categories.name == category)
    else:
        dbq = db.query(models.Products)
    return dbq.offset(skip).limit(limit).all()


def get_product(db: Session, product_id: int):
    return db.query(models.Products).filter(models.Products.id == product_id).first()


def get_card_font(db: Session):
    return db.query(models.CardFont).all()


def get_card_decorations(db: Session):
    return db.query(models.CardDecorations).all()


def get_orders(db: Session, user_id: int):
    return db.query(models.Orders).filter(models.Orders.user_id == user_id).all()


def create_order(db: Session, user_id: int, amount: float, timestamp: int):
    db_order = models.Orders(
        user_id=user_id,
        amount=amount,
        created_at=timestamp,
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order.id


def create_order_product(db: Session, order_id: int, product_id: int, quantity: int, timestamp: int):
    db_order_product = models.OrderDetails(
        order_id=order_id,
        type_id=Types.product,
        product_id=product_id,
        quantity=quantity,
        created_time=timestamp,
    )
    db.add(db_order_product)
    db.commit()
    db.refresh(db_order_product)
    return db_order_product


def create_order_card(db: Session, order_id: int, card_id: int, timestamp: int):
    db_order_card = models.OrderDetails(
        order_id=order_id,
        type_id=Types.card,
        card_id=card_id,
        quantity=1,
        created_time=timestamp,
    )
    db.add(db_order_card)
    db.commit()
    db.refresh(db_order_card)
    return db_order_card


def get_cart(db: Session, cart_id: int):
    return db.query(models.Carts).filter(models.Carts.id == cart_id).first()


def get_carts(db: Session, user_id: int):
    return db.query(models.Carts).filter(models.Carts.user_id == user_id).all()


def update_cart(db: Session, cart: schemas.CartsUpdateQuantity):
    db.query(models.Carts).filter(models.Carts.id == cart.id).update({'quantity': cart.quantity})
    db.commit()
    return db.query(models.Carts).filter(models.Carts.id == cart.id).first()


def create_cart_with_product(db: Session, cart: schemas.ProductToCarts, user_id: int, timestamp: int):
    db_cart = models.Carts(
        user_id=user_id,
        type_id=Types.product,
        product_id=cart.id,
        quantity=cart.quantity,
        created_time=timestamp,
    )
    db.add(db_cart)
    db.commit()
    db.refresh(db_cart)
    return db_cart


def delete_cart(db: Session, cart_id: int):
    db.query(models.Carts).filter(models.Carts.id == cart_id).delete()
    db.commit()
    return True


def get_cards(db: Session, user_id: int):
    return db.query(models.Cards).filter(models.Cards.user_id == user_id).all()


def create_card(db: Session, card: schemas.Card, user_id: int):
    db_card = models.Cards(
        user_id=user_id,
        name=card.name,
        front=card.front,
        back=card.back,
        price=0,
    )
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card


def create_cart_with_card(db: Session, card_id: int, user_id: int, timestamp: int):
    db_cart = models.Carts(
        user_id=user_id,
        type_id=Types.card,
        card_id=card_id,
        quantity=1,
        created_time=timestamp,
    )
    db.add(db_cart)
    db.commit()
    db.refresh(db_cart)
    return db_cart
