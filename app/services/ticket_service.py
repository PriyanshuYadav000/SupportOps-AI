from uuid import uuid4

from app.schemas.ticket import TicketCreate, TicketTriageResult


def triage_ticket(ticket: TicketCreate) -> TicketTriageResult:
    """Create an initial ticket result.

    Classification and priority are placeholders until the ML model is added.
    """
    return TicketTriageResult(
        ticket_id=f"TKT-{uuid4().hex[:10].upper()}",
        customer_id=ticket.customer_id,
        category="Unclassified",
        priority="Medium",
        status="received",
    )
