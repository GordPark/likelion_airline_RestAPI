"""
{
 "firstName": "string",
 "lastName": "string",
 "email": "string",
 "password": "string"
}
 -> DB 유저 정보 저장
{
 "message": "회원가입 성공",
}
"""

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from models import UserModel,Base, UserCreate, User, UserUpdate
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from database import get_db

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     async with engine.begin() as conn:
#         # 데이터베이스 테이블 생성
#         await conn.run_sync(Base.metadata.create_all)
    
#     try:
#         yield  # 여기에서 FastAPI 앱이 실행되는 동안 컨텍스트를 유지합니다.
#     finally:
#         # 비동기 데이터베이스 연결 종료
#         await engine.dispose()

app = FastAPI()  # lifespan=lifespan

origins = [
    '*',
    "http://localhost",
    "http://localhost:3000",
    # Add other origins as needed
]
# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/signup")
def signup(user:UserModel, db: Session = Depends(get_db)):
    # DB저장코드 
    print("DB에 저장 중....")
    return {"message": "회원가입 성공"}

# @app.get("/users", response_model=List[UserModel])
# async def read_products(db: Session = Depends(get_db)):
#     result = await db.execute(select(UserModel))
#     products = result.scalars().all()
#     return products


# ----로그인
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from jose import JWTError, jwt
# from datetime import datetime, timedelta
# from passlib.context import CryptContext

# # 토큰 생성 및 검증을 위한 클래스
# class Token:
#     def __init__(self, expires_delta: timedelta):
#         self.expires_delta = expires_delta

#     def create_access_token(self, data: dict):
#         to_encode = data.copy()
#         expire = datetime.utcnow() + self.expires_delta
#         to_encode.update({"exp": expire})
#         encoded_jwt = jwt.encode(to_encode, "secret", algorithm="HS256")
#         return encoded_jwt

#     def decode_token(self, token: str):
#         try:
#             payload = jwt.decode(token, "secret", algorithms=["HS256"])
#             return payload
#         except JWTError:
#             return None



# # 토큰 유효시간 설정 (예: 15분)
# ACCESS_TOKEN_EXPIRE_MINUTES = 15

# # 토큰 생성 객체 생성
# token_handler = Token(expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))

# # OAuth2PasswordBearer 인스턴스 생성
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# # 사용자 검증 함수
# def authenticate_user(username: str, password: str):
#     user = get_user(username)
#     if not user:
#         return False
#     if not verify_password(password, user["hashed_password"]):
#         return False
#     return user

# # 사용자 가져오는 함수
# def get_user(username: str):
#     if username in fake_users_db:
#         user_dict = fake_users_db[username]
#         return User(**user_dict)

# # 비밀번호 확인 함수
# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)

# # 토큰 생성 엔드포인트
# @app.post("/token")
# async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = authenticate_user(form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(status_code=401, detail="Incorrect username or password")
#     access_token = token_handler.create_access_token(data={"sub": user.username})
#     return {"access_token": access_token, "token_type": "bearer"}

# # 보호된 엔드포인트
# @app.get("/users/me")
# async def read_users_me(token: str = Depends(oauth2_scheme)):
#     payload = token_handler.decode_token(token)
#     if not payload:
#         raise HTTPException(status_code=401, detail="Invalid token")
#     return {"username": payload.get("sub")}



# @app.post("/login")
# def login(email,password,user:UserModel):
#     print("login")
#     return {"message": "로그인성공", 'token': token,"user": user,}
