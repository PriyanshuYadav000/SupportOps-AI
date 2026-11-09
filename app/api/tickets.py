from fastapi import APIRouter, status

from app.schemas.ticket import TicketCreate, TicketTriageResult
from app.services.ticket_service import triage_ticket

router = APIRouter(prefix="/tickets", tags=["Tickets"])


@router.post(
    "/triage",
    response_model=TicketTriageResult,
    status_code=status.HTTP_201_CREATED,
    summary="Submit a support ticket for triage",
)
def create_ticket(ticket: TicketCreate) -> TicketTriageResult:
    return triage_ticket(ticket)
