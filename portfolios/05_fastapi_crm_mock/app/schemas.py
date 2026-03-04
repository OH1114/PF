from pydantic import BaseModel


class TicketIn(BaseModel):
    customer_name: str
    message: str


class TicketOut(BaseModel):
    category: str
    priority: str
