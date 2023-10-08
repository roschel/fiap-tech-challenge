from fastapi import FastAPI

from adapter.api.controllers.auth_controller import AuthController
from adapter.api.controllers.category_controller import CategoryController
from adapter.api.controllers.client_controller import ClientController
from adapter.api.controllers.product_controller import ProductController
from adapter.api.controllers.user_controller import UserController
from core.application.use_cases.category.category_case import CategoryCase
from core.application.use_cases.client.client_case import ClientCase
from core.application.use_cases.product.product_case import ProductCase
from core.application.use_cases.user.user_case import UserCase
from scripts.populate_database import populate

app = FastAPI(title="Tasty Delivery")

# Users
user_controller = UserController(UserCase)

# Categories
category_controller = CategoryController(CategoryCase)

# Products
products_controller = ProductController(ProductCase)

# Clients
clients_controller = ClientController(ClientCase)

# Authentication
auth_controller = AuthController()

app.include_router(clients_controller.router)
app.include_router(user_controller.router)
app.include_router(category_controller.router)
app.include_router(products_controller.router)
app.include_router(auth_controller.router)


@app.on_event("startup")
async def populate_database():
    populate()
