
from pydantic import BaseModel, EmailStr, constr
class UserValidator(BaseModel):
  email: EmailStr
  password: constr(min_length=8, max_length=16)
  role: str = 'USER'or 'ADMIN' or 'EVENT_ORGANIZER'
  name: str
  password: str
  
  