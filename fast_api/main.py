# backend/main.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# CORS 설정 (개발 중에만 허용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # Vue 개발 서버 주소
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API 엔드포인트
@app.get("/api/events")
async def read_events():
    return [
        {"date": "2023-10-01", "event": "미팅"},
        {"date": "2023-10-05", "event": "프로젝트 마감"},
    ]

# 정적 파일 서빙
app.mount("/static", StaticFiles(directory="dist/static"), name="static")

# 모든 경로에 대해 index.html 반환
@app.get("/{full_path:path}")
async def serve_vue_app(full_path: str):
    file_path = os.path.join('dist', 'index.html')
    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        return {"message": "File not found"}