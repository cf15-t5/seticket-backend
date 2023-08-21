from pydantic import BaseModel

class CreateNewTicketValidator(BaseModel):
    event_id: int
    