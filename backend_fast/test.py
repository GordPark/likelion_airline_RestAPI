# from fastapi import Depends, FastAPI, HTTPException
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from jose import JWTError, jwt
# from passlib.context import CryptContext
# from pydantic import BaseModel
# from datetime import datetime, timedelta

# # 임시로 사용할 사용자 데이터
# fake_users_db = {
#     "johndoe": {
#         "username": "johndoe",
#         "full_name": "John Doe",
#         "email": "johndoe@example.com",
#         "hashed_password": "$2b$12$5l1wCZqSYeFMd0u/KQoq5OjLJcT8c3V6Hj3P9bjqH/j6wU7J8qUbq",
#         "disabled": False,
#     }
# }

# # 비밀번호 해싱 및 인증 관련 설정
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# # 사용자 모델
# class User(BaseModel):
#     username: str
#     email: str
#     full_name: str
#     disabled: bool = None

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

# # FastAPI 애플리케이션 생성
# app = FastAPI()

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
