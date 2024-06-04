# # 루트에 main을 둔다
# # main에는 회원가입과 
# # 단일체계 하나는 하나 위반
# # 메인에 다 때려박아도됨

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}



# async def read_products(db: Session = Depends(get_db))