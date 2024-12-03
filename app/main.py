import uvicorn
from fastapi import FastAPI
import os
from app.routes.student_routes import router as student_router

app = FastAPI()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Default to 8000 if $PORT is not set
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=True)

app.include_router(student_router, prefix="/api")
