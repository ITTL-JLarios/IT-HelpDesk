from typing import Annotated
from datetime import datetime

from fastapi import APIRouter, HTTPException, status, Depends

from api.models.user import User, UserInDB
from api.models.ticket import ( TicketView,
                                Ticket,
                                TicketInDB,
                                TicketBase,
                                Event,
                                Status)
from api.dependencies.auth import (get_current_active_user,
                                   get_current_admin_active_user,
                                   get_password_hash)

from settings import tickets


router = APIRouter(
    prefix="/ticket",
    tags=["Tickets"],
    responses={404: {"description": "Not found"}},
)

# General Requests
@router.get("/id/{id}")
async def find_ticket(
    id: str
):
    ticket = search_ticket_by_id(id)

    if not ticket:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                      detail="Ticket Not Found")
        
    return TicketBase(**ticket)

@router.post('/new/')
async def create_ticket(ticket: TicketBase):
    if is_ticket_duplicated(dict(ticket)):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Ticket Duplicated")
    return ticket

# IT Request
@router.get("/ee/{ee_name}")
async def ee_tickets(
        current_user: Annotated[User, Depends(get_current_active_user)],
        ee_name: str
):
    if not search_ee_tickets(ee_name):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Tickets not found")
    
    return search_ee_tickets(ee_name)

@router.post("/id/")
async def add_event(
        current_user: Annotated[User, Depends(get_current_active_user)],
        id: str,
        note: str,
        tag: Status
):
    #TODO: Make this ask for ticket list from DB and serialize it for response
    if not search_ee_tickets(id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Ticket not found")

    event = Event(username=current_user.username,
                  notes=note,
                  tag=tag)
    
    #TODO: Make this work and placed in a DB and verify that was saved on DB
    
    return event

@router.patch("/id/")
async def add_event(
        current_user: Annotated[User, Depends(get_current_active_user)],
        id: str,
        note: str,
):
    if not search_ee_tickets(id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Ticket not found")
    
    #TODO: Make this update Ticket from DB and serialize it for response
    return {"note": note}
    
# Admin Requests
@router.get("/list/")
async def ticket_list(
    current_user: Annotated[User, Depends(get_current_admin_active_user)],
):
    #TODO: Make this ask for ticket list from DB and serialize it for response
    return [TicketBase(**ticket) for ticket in tickets]


def search_ticket_by_id(id: str) -> bool | dict:
    """
        Check if ticket is on DB and get its info

        args:
            id <str>: The ticket # or ID
        return:
            <bool | dict> The ticket info from db if exist and False if not.
    """
    #TODO: Make this functional work with db to get the ticket
    if id in tickets[0]["ee_name"]:
        return tickets[0]
    return False

def search_ee_tickets(ee_name: str) -> bool | dict:
    """
        Check if there is any ticket on DB and get their info

        args:
            ee_name <str>: Employee Name
        return:
            <bool | list[dict]> The tickets info from db if exist and False if not.
    """
    #TODO: Make this functional work with db to get the ticket
    if ee_name in tickets[0]["ee_name"]:
        return [ ticket for ticket in filter(
            lambda x: x["ee_name"] == ee_name ,tickets)]
    
    return False

def is_ticket_duplicated(ticket: dict) -> bool:
    """
        Check if there is any ticket on DB and get their info

        args:
            ticket <dict>: Ticket base Iformation
        return:
            <bool | list[dict]> The tickets info from db if exist and False if not.
    """

    #TODO: Make this functional work with db to get the ticket
    my_ticket = list(filter(lambda x: x["ee_name"] == ticket["ee_name"], tickets))
    if ticket["issue"] == (my_ticket[len(my_ticket)-1])["issue"]:
        return True
    return False