from fastapi import FastAPI

from tasty_delivery.adapter.api.controllers.category_controller import CategoryController
from tasty_delivery.adapter.api.controllers.product_controller import ProductController
from tasty_delivery.adapter.api.controllers.user_controller import UserController
from tasty_delivery.core.application.use_cases.category.category_case import CategoryCase
from tasty_delivery.core.application.use_cases.product.product_case import ProductCase
from tasty_delivery.core.application.use_cases.user.user_case import UserCase
from tasty_delivery.scripts.populate_database import populate

app = FastAPI()

# Users
user_controller = UserController(UserCase)

# Categories
category_controller = CategoryController(CategoryCase)

# Products
products_controller = ProductController(ProductCase)

app.include_router(user_controller.router)
app.include_router(category_controller.router)
app.include_router(products_controller.router)


@app.on_event("startup")
async def populate_database():
    populate()
