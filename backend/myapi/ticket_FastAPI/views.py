# # 데이터를 받음 > 모델로 > 뷰로 / 중간이 controler

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class StudyGroup(BaseModel):
#     name: str
#     topic: str
#     max_members: int

# @app.post("/study-groups")
# def create_study_group(group: StudyGroup):
#     return {"message": "Study group created successfully", "group": group}