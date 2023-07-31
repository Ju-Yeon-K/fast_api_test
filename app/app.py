import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .db.models import item_models, user_models
from .routers import item, user

# 환경변수 경로 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = FastAPI(swagger_ui_parameters={
    'persistAuthorization': True
    })

# 접근 허용 url
origins = [
    "*",
    # "http://localhost",
    # "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# env 잘 로드하는지 테스트
# @app.get("/")
# def read_env():
#     test_env = os.environ["TEST_ENV"]
#     return {"res":test_env}

# router 연결
app.include_router(user.router)
app.include_router(item.router)
