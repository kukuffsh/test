from fastapi import APIRouter, HTTPException, Depends
from app.db_requests import create_new_user, user_login
from app.db_models import Post, User
from app.models import PostModel
from sqlalchemy.orm import Session
from app.config.database import create_session
from app.auth.auth_bearer import JWTBearer
from app.db_requests import get_user_page, create_post
from app.auth.auth_handler import signJWT, token_response, decodeJWT

router = APIRouter(tags=['UserPage'])


@router.get("/{user}", dependencies=[Depends(JWTBearer())], tags=[""])
async def user_page(db: Session = Depends(create_session), jwt: JWTBearer = Depends(JWTBearer())):
    uid = decodeJWT(jwt).get('user_id')
    return get_user_page(uid, db)

@router.post("/create_post", dependencies=[Depends(JWTBearer())], tags=[""])
async def new_post(post: PostModel, db: Session = Depends(create_session), jwt: JWTBearer = Depends(JWTBearer())):
    uid = decodeJWT(jwt).get('user_id')
    return create_post(post, uid, db)
