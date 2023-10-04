from tasty_delivery.adapter.database.db import get_db
from tasty_delivery.core.application.use_cases.category.category_case import CategoryCase
from tasty_delivery.core.application.use_cases.product.product_case import ProductCase
from tasty_delivery.core.application.use_cases.user.user_case import UserCase
from tasty_delivery.core.domain.entities.category import Category
from tasty_delivery.core.domain.entities.product import Product
from tasty_delivery.core.domain.entities.user import User


def populate():
    categories_mock = [
        Category(nome="Lanches"),
        Category(nome="Sobremesa"),
        Category(nome="Refrigerantes"),
    ]

    for category in categories_mock:
        result = CategoryCase(next(get_db())).get_all()

        if result:
            break

        result = CategoryCase(next(get_db())).create(category)
        if result.nome == "Lanches":
            ProductCase(next(get_db())).create(Product(nome="BigMc", category_id=str(result.id)))
            ProductCase(next(get_db())).create(Product(nome="Whooper", category_id=str(result.id)))
            ProductCase(next(get_db())).create(Product(nome="Cheedar", category_id=str(result.id)))
        elif result.nome == "Sobremesa":
            ProductCase(next(get_db())).create(Product(nome="Casquinha", category_id=str(result.id)))
        else:
            ProductCase(next(get_db())).create(Product(nome="Coca Cola", category_id=str(result.id)))
            ProductCase(next(get_db())).create(Product(nome="Guaraná", category_id=str(result.id)))
            ProductCase(next(get_db())).create(Product(nome="Fanta Laranja", category_id=str(result.id)))

    mock_user = [
        User(nome="João", cpf="11122233344", email="joao@email.com"),
        User(nome="Victor", cpf="2223334455", email="victor@email.com"),
        User(nome="Tais", cpf="33344455566", email="tais@email.com"),
        User(nome="Augusto", cpf="44455566677", email="augusto@email.com"),
    ]

    for user in mock_user:
        result = UserCase(next(get_db())).get_all()

        if result:
            break
        UserCase(next(get_db())).create(user)
