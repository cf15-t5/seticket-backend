from pydantic import BaseModel, constr

class CreateNewTicketValidator(BaseModel):
    event_id: int
    
class AttendTicketValidator(BaseModel):
    ticket_code: constr(min_length=6, max_length=6)