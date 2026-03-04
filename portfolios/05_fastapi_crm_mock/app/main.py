from fastapi import FastAPI

from .schemas import TicketIn, TicketOut
from .service import classify_message

app = FastAPI(title="CRM Automation Mock API")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/tickets/classify", response_model=TicketOut)
def classify(ticket: TicketIn) -> TicketOut:
    return classify_message(ticket.message)
