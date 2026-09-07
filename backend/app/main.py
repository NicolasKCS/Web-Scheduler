from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# We will uncomment this once routes.py is created
# from app.routes import router as monitor_router

app = FastAPI(
    title="CronOps API",
    description="Backend for Scheduled Uptime & API Monitor",
    version="1.0.0"
)

# Configure CORS for the React frontend (Vite defaults to port 5173)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(monitor_router, prefix="/api/v1")

@app.get("/health")
async def health_check():
    """
    Basic health check endpoint to verify the API is running.
    """
    return {"status": "ok", "message": "CronOps API is ready"}