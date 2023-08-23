
from pydantic import BaseModel, EmailStr, constr
from enum import Enum
class ROLE(str, Enum):
  ADMIN = 'ADMIN'
  USER = 'USER'
  EVENT_ORGANIZER = 'EVENT_ORGANIZER'

class STATUS(str, Enum):
  INACTIVE = 'INACTIVE'
  ACTIVE = 'ACTIVE'
  REJECTED = 'REJECTED'
class RegisterValidator(BaseModel):
  email: EmailStr
  password: constr(min_length=8, max_length=16)
  role: ROLE 
  name: str
  password: str

class LoginValidator(BaseModel):
  email: EmailStr
  password: constr(min_length=8, max_length=16)

class VerifyValidator(BaseModel):
  user_id: int
  status: STATUS