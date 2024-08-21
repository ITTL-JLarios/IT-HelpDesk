from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Depends

from api.models.user import User, UserInDB
from api.models.ticket import TicketView, Ticket, TicketInDB, TicketBase
from api.dependencies.auth import (get_current_active_user,
                                   get_current_admin_active_user,
                                   get_password_hash)

from settings import tickets


router = APIRouter(
    prefix="/ticket",
    tags=["Tickets"],
    dependencies=[Depends(get_current_active_user)],
    responses={404: {"description": "Not found"}},
)


@router.get("/list/")
async def ticket_list(
    current_user: Annotated[User, Depends(get_current_admin_active_user)],
):
    #TODO: Make this ask for ticket list from DB and serialize it for response
    return [TicketBase(**ticket) for ticket in tickets]

@router.get("/{id}")
async def find_ticket(
    current_user: Annotated[User, Depends(get_current_active_user)],
    id: str
):
    ticket = search_ticket_by_id(id)

    if not ticket:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                      detail="Ticket Not Found")
        
    return TicketBase(**ticket)



def search_ticket_by_id(id: str):
    """
        Check if ticket is on DB and ge its info

        args:
            id <str>: The ticket # or ID
        return:
            <bool | dict> The ticket info from db if exist and False if not.
    """
    # TODO: Make this functional work with db to get the ticket
    if id in tickets[0]["ee_name"]:
        return tickets[0]
    return False