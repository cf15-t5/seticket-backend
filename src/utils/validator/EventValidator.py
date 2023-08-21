from pydantic import BaseModel
from typing import Optional
from enum import Enum
class CreateNewEventValidator(BaseModel):
  title: str
  price: int
  description: str
  date_of_event: str
  number_of_ticket: int
  category_id: int
  @classmethod
  def as_form(cls, **kwargs):
    return cls(**kwargs)


class UpdateEventValidator(BaseModel):
  id: int
  title: Optional[str] = None
  price: Optional[int] = None
  description: Optional[str] = None
  date_of_event: Optional[str] = None
  number_of_ticket: Optional[int] = None
  @classmethod
  def as_form(cls, **kwargs):
    return cls(**kwargs)
  
  
class VerifyEventValidator(BaseModel):
  id: int
  status: str



class DeleteEventValidator(BaseModel):
  id:str
  
  
class STATUS(str,Enum):
  APPROVED="APPROVED"
  REJECTED="REJECTED"
  
class VerifyEventValidator(BaseModel):
  id:int
  status:STATUS