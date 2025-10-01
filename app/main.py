import os
import uvicorn
from fastapi import FastAPI, status
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from app.api.routes import router

port = int(os.getenv("PORT", 8000))

# Create the FastAPI app
app = FastAPI(
    title="Enigma Machine", description="A web-based Enigma Machine simulator"
)

# Include the API routes
app.include_router(router)

# Serve static files (CSS, JS, images)
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def serve_frontend():
    """Serve the main HTML page"""
    return FileResponse("static/index.html")


@app.get("/health")
async def health_check():
    """Health check endpoint for Railway"""
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "status": "healthy",
            "service": "enigma-machine",
            "port": port,
            "message": f"Running on port {port}",
        },
    )


if __name__ == "__main__":
    print(f"🚀 Starting Enigma Machine on port {port}")
    print(f"🌍 Environment: {os.getenv('RAILWAY_ENVIRONMENT', 'local')}")
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, log_level="info")
