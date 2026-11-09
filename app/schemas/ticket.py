from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class TicketCreate(BaseModel):
    """Payload submitted when a customer opens a support ticket."""

    model_config = ConfigDict(str_strip_whitespace=True)

    customer_id: str = Field(min_length=1, max_length=64)
    subject: str = Field(min_length=3, max_length=200)
    description: str = Field(min_length=10, max_length=5000)


class TicketTriageResult(BaseModel):
    """Initial triage result returned by the service."""

    ticket_id: str
    customer_id: str
    category: str
    priority: Literal["Low", "Medium", "High"]
    status: Literal["received"]
