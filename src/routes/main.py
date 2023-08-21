from src.controllers.UserController import UserApp
from src.controllers.AuthController import AuthApp
from src.controllers.EventController import EventApp
from src.controllers.CategoryController import CategoryApp
from src.controllers.TicketController import TicketApp
routes = [
  { "url": "/users", "name": UserApp },
  {"url": "/auth", "name": AuthApp},
  {"url":"/categories","name":CategoryApp},
  {"url":"/events","name":EventApp},
  {"url":"/tickets","name":TicketApp}
]
