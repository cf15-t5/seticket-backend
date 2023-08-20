from src.controllers.UserController import UserApp
from src.controllers.AuthController import AuthApp
from src.controllers.EventController import EventApp
from src.middlewares.AuthMiddleware import isAuthenticated
routes = [
  { "url": "/users", "name": UserApp },
  {"url": "/auth", "name": AuthApp},
  {"url":"/events","name":EventApp},
]
