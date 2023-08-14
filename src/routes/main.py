from flask import Blueprint
from src.controllers.UserController import UserApp
from src.controllers.AuthController import AuthApp
routes = [
  { "url": "/user", "name": UserApp},
  {"url": "/auth", "name": AuthApp}
]