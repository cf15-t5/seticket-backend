from pydantic import BaseModel
from typing import Optional
class CreateNewCategoryValidator(BaseModel):
    name: str

class UpdateCategoryValidator(BaseModel):
    id: int
    name: Optional[str]=None
    
class DeleteCategoryValidator(BaseModel):
    id:int