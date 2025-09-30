from fastapi import APIRouter, HTTPException, Depends
from app.api.models import EncryptRequest, EncryptResponse
from app.services.enigma_service import EnigmaService

# Create router instance
router = APIRouter()


def get_enigma_service() -> EnigmaService:
    """Dependency injection for EnigmaService"""
    return EnigmaService()


@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


@router.post("/api/encrypt", response_model=EncryptResponse)
async def encrypt_message(
    request: EncryptRequest, enigma_service: EnigmaService = Depends(get_enigma_service)
):
    """Encrypt a message using the Enigma machine"""
    try:
        return enigma_service.encrypt_message(request)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.get("/api/config")
async def get_machine_config(
    enigma_service: EnigmaService = Depends(get_enigma_service),
):
    """Get available rotors and reflectors"""
    return enigma_service.get_available_configurations()
