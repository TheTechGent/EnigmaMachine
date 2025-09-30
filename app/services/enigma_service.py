from app.enigma.machine import Machine as EnigmaMachine
from app.enigma.keyboard import Keyboard
from app.enigma.plugboard import Plugboard
from app.enigma.rotor import Rotor
from app.enigma.reflector import Reflector
from app.enigma.configuration import e_rotors, e_reflectors
from app.api.models import EncryptRequest, EncryptResponse


class EnigmaService:
    """Service for Enigma machine operations"""

    def __init__(self):
        self.rotor_configs = {
            "I": e_rotors.I,
            "II": e_rotors.II,
            "III": e_rotors.III,
            "IV": e_rotors.IV,
            "V": e_rotors.V,
        }
        self.reflector_configs = {
            "A": e_reflectors.A,
            "B": e_reflectors.B,
            "C": e_reflectors.C,
        }

    def validate_configuration(self, request: EncryptRequest):
        """Validate Enigma configuration"""
        errors = []

        if request.rotor1 not in self.rotor_configs:
            errors.append(f"Invalid rotor1: {request.rotor1}")
        if request.rotor2 not in self.rotor_configs:
            errors.append(f"Invalid rotor2: {request.rotor2}")
        if request.rotor3 not in self.rotor_configs:
            errors.append(f"Invalid rotor3: {request.rotor3}")
        if request.reflector not in self.reflector_configs:
            errors.append(f"Invalid reflector: {request.reflector}")

        if errors:
            raise ValueError("; ".join(errors))

    def create_machine(self, request: EncryptRequest) -> EnigmaMachine:
        """Create and configure an Enigma machine"""
        self.validate_configuration(request)

        # Create components
        keyboard = Keyboard()
        plugboard = Plugboard(request.plugboard)
        rotor1 = Rotor(self.rotor_configs[request.rotor1])
        rotor2 = Rotor(self.rotor_configs[request.rotor2])
        rotor3 = Rotor(self.rotor_configs[request.rotor3])
        reflector = Reflector(self.reflector_configs[request.reflector])

        # Create machine
        machine = EnigmaMachine(
            reflector=reflector,
            rotor1=rotor1,
            rotor2=rotor2,
            rotor3=rotor3,
            plugboard=plugboard,
            keyboard=keyboard,
        )

        # Configure machine
        machine.set_rings(tuple(request.rings))
        machine.set_position(request.position)

        return machine

    def encrypt_message(self, request: EncryptRequest) -> EncryptResponse:
        """Encrypt a message using the Enigma machine"""
        machine = self.create_machine(request)

        # Encrypt message
        encrypted = machine.encipher_message(request.message)

        # Get final rotor positions
        final_positions = [
            machine.rotor1.left[0],
            machine.rotor2.left[0],
            machine.rotor3.left[0],
        ]

        return EncryptResponse(
            encrypted_message=encrypted, rotor_positions=final_positions
        )

    def get_available_configurations(self) -> dict:
        """Get available rotors and reflectors"""
        return {
            "rotors": list(self.rotor_configs.keys()),
            "reflectors": list(self.reflector_configs.keys()),
        }
