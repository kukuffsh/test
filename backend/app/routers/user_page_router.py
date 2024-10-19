from fastapi import APIRouter, Depends
from app.db_models import Post, User
from app.models import PostModel
from sqlalchemy.orm import Session
from app.config.database import create_session
from app.auth.auth_bearer import JWTBearer
from app.db_requests import get_user_page, create_post
from app.auth.auth_handler import decodeJWT

router = APIRouter(tags=['UserPage'])


@router.get("/{userlogin}", dependencies=[Depends(JWTBearer())], tags=[""])
def user_page(userlogin: str = '', db: Session = Depends(create_session), jwt: JWTBearer = Depends(JWTBearer())) -> User:
    uid = decodeJWT(jwt).get('user_id')
    userPage = get_user_page(uid, db)
    userlogin = userPage('login')
    return userPage

@router.post("/create_post", dependencies=[Depends(JWTBearer())], tags=[""])
def new_post(post: PostModel, db: Session = Depends(create_session), jwt: JWTBearer = Depends(JWTBearer())) -> Post:
    uid = decodeJWT(jwt).get('user_id')
    return create_post(post, uid, db)
