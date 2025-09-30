from pydantic import BaseModel
from typing import List


class EncryptRequest(BaseModel):
    message: str
    rotor1: str = "I"
    rotor2: str = "II"
    rotor3: str = "III"
    reflector: str = "B"
    position: str = "AAA"
    rings: List[int] = [1, 1, 1]
    plugboard: List[str] = []


class EncryptResponse(BaseModel):
    encrypted_message: str
    rotor_positions: List[str]
