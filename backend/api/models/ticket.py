from datetime import datetime
from pydantic import BaseModel
from typing import Annotated, Union
from enum import Enum

class Status(Enum):
    res="Resolved"
    test="Test"
    rev="Review"
    closed="Closed"
    open="Open"


class Event(BaseModel):
    username: str
    timestamp: datetime
    notes: str
    tag: Union[Status, None] = None

class TicketBase(BaseModel):
    ee_name: str
    email: Union[str, None] = None
    workstation: Union[str, None] = None
    issue: str
    equipment: str
    status: Union[Status, None] = Status.open

class Ticket(TicketBase):
    event_id: Union[list, str, None] = None

class TicketInDB(Ticket):
    id: Union[str, None] = None
    timestamp: datetime

class TicketView(TicketBase):
    id: str
    timestamp: datetime
    event: Union[list, Event, None] = None