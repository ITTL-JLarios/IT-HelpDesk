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

@router.get("/me/", response_model=User)
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user

@router.get("/me/items/")
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return [{"item_id": "Foo", "owner": current_user.username}]

@router.post("/register")
async def create_new_user(
    current_user: Annotated[User, Depends(get_current_admin_active_user)],
    new_user: UserInDB
):
    #TODO: change code for real DB instead fake one
    if new_user.username.lower() in fake_users_db:
        raise HTTPException(status_code=400, detail="User already Exist")
    
    new_user.hashed_password = get_password_hash(new_user.hashed_password)

    # TODO: Save data in DB
    return User(**dict(new_user))

@router.patch("/recovery-password", status_code=202)
async def update_user_password(
    current_user: Annotated[User, Depends(get_current_admin_active_user)],
    password: str,
):
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
