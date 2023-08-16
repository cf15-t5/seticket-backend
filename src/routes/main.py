from src.controllers.UserController import UserApp
from src.controllers.AuthController import AuthApp
from src.middlewares.AuthMiddleware import isAuthenticated
routes = [
  { "url": "/user", "name": UserApp },
  {"url": "/auth", "name": AuthApp}
]
