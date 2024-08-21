from datetime import datetime, timedelta, timezone
from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Depends

from api.models.user import User, UserInDB
from api.dependencies.auth import (get_current_active_user,
                                   get_current_admin_active_user,
                                   get_password_hash)

from settings import fake_users_db

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    dependencies=[Depends(get_current_active_user)],
    responses={404: {"description": "Not found"}},
)

# Users Petitions
@router.get("/me/", response_model=User)
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user


# Admin Petitions
@router.post("/register")
async def create_new_user(
    current_user: Annotated[User, Depends(get_current_admin_active_user)],
    new_user: UserInDB
):
    #TODO: change code for real DB instead fake one
    user = user_exist(new_user.username)
    if type( user ) == dict:
        raise HTTPException(status_code=400, detail="User already Exist")
    
    new_user.hashed_password = get_password_hash(new_user.hashed_password)

    # TODO: Save data in DB
    return User(**dict(new_user))

@router.patch("/recovery-password", status_code=202)
async def update_user_password(
    current_user: Annotated[User, Depends(get_current_admin_active_user)],
    username: str,
    password: str,
):
    if not user_exist(username):
        raise HTTPException(status_code=400,
                            detail="User Doesn't Exist")
    if len(password) < 8:
        raise HTTPException(status_code=400,
                            detail="Password Lenght should be greater than 8 characters")
    # TODO: change code for real DB instead fake one

    hashed_password = get_password_hash(password)

    # TODO: Add hashed password into DB
    try:
        pass
    except:
        raise HTTPException(status_code=400,
                            detail="")

    return {"message": "Password Updated Successfully"}

@router.delete("/delete/{username}", status_code=202)
async def delete_user(
    current_user: Annotated[User, Depends(get_current_admin_active_user)],
    username: str
):
    # TODO: Add delete DB function to delete user.
    return True


# General Functions
def user_exist(username: str) -> bool | dict:
    """
        Check if username already exist in db.

        Args:
            username <str>: The user's Username

        Return:
            <bool | dict> user dict if user exist and else False.
    """
    if username.lower() in fake_users_db:
        return fake_users_db[username.lower()]
    return False
