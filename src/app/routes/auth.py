from fastapi import APIRouter , HTTPException , status
from app.schemas.user import UserLogin
from app.utils.jwt_handler import encode_data

from app.in_memory_users.users_list import get_user_list, get_admin_user_list
from app.utils.logger import logger


router = APIRouter()



@router.post("/login")
def login(user: UserLogin):
    logger.info(f"Login attempt for username: {user.user_name}")

    for u in get_user_list():
        if user.user_name == u.user_name and user.password == u.password:
            logger.info(f"Student login successful: {user.user_name}")

            payload = {
                "user_id": u.user_id,
                "role": "student"
            }
            token = encode_data(payload)
            logger.debug(f"JWT token generated for student user_id={u.user_id}")
            return {
                "success": True,
                "token": token
            }

    for u in get_admin_user_list():
        if user.user_name == u.user_name and user.password == u.password:
            logger.info(f"Admin login successful: {user.user_name}")
            payload = {
                "user_id": u.user_id,
                "role": "admin"
            }
            token = encode_data(payload)

            logger.debug(f"JWT token generated for admin user_id={u.user_id}")
            return {
                "success": True,
                "token": token
            }


    raise HTTPException(status_code=401,detail="Unauthorized Credentials")


    