from fastapi import Depends, HTTPException, status

from app.core.depends import UserDepends

user_depends = UserDepends()


def require_roles(*roles):

    async def checker(
        current_user=Depends(user_depends.get_current_user)
    ):
        print("CURRENT_USER",current_user)
        if current_user["role"] not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Role not allowed",
            )

        return current_user

    return checker