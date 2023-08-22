from pydantic import BaseModel, constr, EmailStr
class UpdateProfileValidator(BaseModel):
  name: str
  email: EmailStr
  password: constr(min_length=8, max_length=16)
  
class UpdateBalanceValidator(BaseModel):
  nominal: int