def user_db_scheme(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "email": user["email"],
        "full_name": user["full_name"],
        "disabled":  user["disabled"],
        "role": user["role"],
    }

def user_scheme(user) -> dict:
    return {
        "username": user["username"],
        "email": user["email"],
        "full_name": user["full_name"],
        "disabled":  user["disabled"],
        "role": user["role"],
    }